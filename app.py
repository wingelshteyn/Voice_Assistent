from sklearn.feature_extraction.text import CountVectorizer  # pip install scikit-learn
from sklearn.linear_model import LogisticRegression
import sounddevice as sd  # pip install sounddevice
import vosk  # pip install vosk

import json

import get_parametrs
import words
from skills import *
import voice
from feeches import datetime_greeting

import silero_tts.silero_tts as stts
from silero_tts.silero_tts import SileroTTS

from threading import Thread

# Спикер
# Get available models
models = SileroTTS.get_available_models()
print("Available models:", models)

# Get available languages
languages = SileroTTS.get_available_languages()
print("Available languages:", languages)

# Get the latest model for a specific language
latest_model = SileroTTS.get_latest_model('ru')
print("Latest model for Russian:", latest_model)

# Get available sample rates for a specific model and language
sample_rates = SileroTTS.get_available_sample_rates_static('ru', latest_model)
print("Available sample rates for the latest Russian model:", sample_rates)

# Supported speakers: ['aidar', 'baya', 'kseniya', 'xenia', 'eugene', 'random']
tts = SileroTTS(model_id='v3_1_ru', language='ru', speaker='xenia', sample_rate=48000, device='cpu')

q = queue.Queue()

model = vosk.Model("vosk")

device = sd.default.device

samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])
confirmation_mode = False
confirmation_func = ''
confirmation_answer = ''

def callback(indata, frames, time, status):
    q.put(bytes(indata))


def recognize(data, vectorizer, clf):
    global confirmation_func, confirmation_mode, confirmation_answer

    if confirmation_mode:
        if 'да' in data or 'конечно' in data:
            voice.speaker('поняла, ' + confirmation_answer)
            exec(confirmation_func + f'()')
        else:
            voice.speaker('запрос отменён')
        confirmation_func = ''
        confirmation_mode = False

    # Проверка на налицие слова "триггера"
    trg = words.TRIGGERS.intersection(data.split())
    if not trg:
        return

    data.replace(list(trg)[0], '')

    text_vector = vectorizer.transform([data]).toarray()[0]
    answer = clf.predict([text_vector])[0]

    func_name = answer.split()[0]

    if 'confirmation' in func_name:
        confirmation_mode = True
        confirmation_answer = answer.replace(func_name, '')
        voice.speaker('вы уверены')
        return
    parametrs = get_parametrs.get_parametrs(func_name, data)

    t = Thread(target=voice.speaker, args=[answer.replace(func_name, '')])
    t.start()

    if parametrs is not None:
        exec(func_name + f'({parametrs})')
        print(func_name + f'({parametrs})')
    else:
        exec(func_name + f'()')
        print(func_name + '()')


def main():
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(list(words.data_set.keys()))

    clf = LogisticRegression()
    clf.fit(vectors, list(words.data_set.values()))

    del words.data_set
    print("Успешно запущено")

    voice.speaker("Привет")

    quite_mode = False

    while quite_mode:
        name = ''
        for e in words.TRIGGERS:
            name = e
            break
        data = name + ' ' + input()
        recognize(data, vectorizer, clf)

    with sd.RawInputStream(samplerate=48000, blocksize=16000, device=device[0], dtype='int16',
                           channels=1, callback=callback):

        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                data = json.loads(rec.Result())['text']
                print(data)
                recognize(data, vectorizer, clf)


if __name__ == '__main__':
    main()
