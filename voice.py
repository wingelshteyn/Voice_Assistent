# import pyttsx3
#
# engine = pyttsx3.init()
# engine.setProperty('rate', 180)
#
#
# def speaker(text):
# 	engine.say(text)
# 	engine.runAndWait()
# 	print(text)
import random

import winsound
from app import tts

r = random.Random()

def speaker(text):
    fragments = text.split('|')
    fragment = fragments[r.randint(0, len(fragments)-1)]

    tts.tts(fragment, "output.wav")

    filename = 'output.wav'
    winsound.PlaySound(filename, winsound.SND_FILENAME)



# =============================================
# from argparse import ArgumentParser
#
# from speechkit import model_repository, configure_credentials, creds

# # Аутентификация через API-ключ.
# configure_credentials(
#    yandex_credentials=creds.YandexCredentials(
#       api_key='b1g70tm5mga4evqtpbkh'
#    )
# )
#
# def speaker(text, export_path):
#    model = model_repository.synthesis_model()
#
#    # Задайте настройки синтеза.
#    model.voice = 'jane'
#    model.role = 'good'
#
#    # Синтез речи и создание аудио с результатом.
#    result = model.synthesize(text, raw_format=False)
#    result.
