import os
import random
import webbrowser
import sys
from pynput.keyboard import Key, Controller
from feeches.Database import Database
from difflib import SequenceMatcher
from pathlib import Path
from feeches import auto_timer
from threading import Thread
import queue
import test_kurs
import datetime
from gtts import gTTS
from silero_tts.silero_tts import transliterate

from sympy import symbols, simplify


import voice

try:
    import requests
except:
    pass

database = Database.get_apps()

def eKurs():
    test_kurs.reg()

def sys_settings():
    # открыть параметры
    keyboard = Controller()
    keyboard.press(Key.cmd)
    keyboard.press('i')
    keyboard.release(Key.cmd)
    keyboard.release('i')


def regedit():
    # открыть редактор реестра
    os.system('start regedit.exe')


def task_dispetcher():
    # открыть диспетчер задач
    os.system("start taskmgr")


def screen_shoot():
    # делает скриншот
    keyboard = Controller()
    keyboard.press(Key.print_screen)
    keyboard.release(Key.print_screen)


def alt_f4():
    # закрывает активное окно
    keyboard = Controller()
    keyboard.press(Key.alt_l)
    keyboard.press(Key.f4)
    keyboard.release(Key.alt_l)
    keyboard.release(Key.f4)


def update_web():
    # обновить страницу
    keyboard = Controller()
    keyboard.press(Key.ctrl_l)
    keyboard.press('r')
    keyboard.release(Key.ctrl_l)
    keyboard.release('r')


def explorer():
    # открыть проводник
    os.system("start explorer")


def downloads():
    # Открыть папку загрузки
    os.system(f'start {str(Path.home() / "Downloads")}')


def random_num(range_=None):
    # назвать случайное число
    if range_ is None:
        voice.speaker("блин, что-то пошло не так")
        return
    if range_[0] >= range_[1]:
        voice.speaker("вы неправильно указали диапазон!")
        return
    num = random.randint(range_[0], range_[1])
    voice.speaker(f'{num}')


def anekdot():
    # рассказать анекдот
    aneks = []
    with open('feeches/anek.txt', encoding='utf-8') as f:
        for line in f:
            if line != '\n':
                aneks.append(line.replace('\n', ''))
    voice.speaker(aneks[random.randint(0, len(aneks)-1)])


def pause():
    # поставить на паузу (через кнопку мультимедиа)
    keyboard = Controller()
    keyboard.press(Key.pause)
    keyboard.release(Key.pause)


def recycle_bin():
    # открыть корзину
    os.system("start shell:RecycleBinFolder")


def browser():
    pass


def search_in_youtube(search_term=None):
    # поиск в ютуб
    if search_term is None:
        voice.speaker("произошла какая-то ошибка")
        return
    # https://www.citilink.ru/results?search_query=
    url = "https://www.youtube.com/results?search_query=" + search_term
    webbrowser.get().open(url)


def appdata():
    # открыть папку roaming (apptata)
    path = os.getenv('APPDATA')
    path = os.path.realpath(path)
    os.startfile(path)


def game():
    pass


def count(req=None):
    # посчитать некоторые выражения и уравнения
    if req is None:
        voice.speaker('Произошла какая-то ошибка!')
        return
    x, y, z = symbols('x y z')
    expr = req
    try:
        simplified_expr = simplify(expr)
        print(simplified_expr)
    except:
        voice.speaker('Произошла какая-то ошибка!')
        return
    voice.speaker(f'{simplified_expr}')

def confirmation_off_pc():
    # Выключение ПК
    os.system('shutdown /s /t 0')
    pass


def confirmation_reset_pc():
    # Перезагрузка ПК
    os.system('shutdown /r /t 0')
    pass

def timer(time=None):
    if time is None:
        voice.speaker('Произошла какая-то ошибка')
        return
    qe = queue.Queue()
    tread = Thread(target=auto_timer.countdown, args=[qe, int(time[0])])
    tread.start()
    while tread.is_alive():  # пока функция выполняется
        if qe.get():
            voice.speaker('Время вышло!')


def confirmation_off_Bot():
    sys.exit()


def some():
    keyboard = Controller()
    keyboard.type('Hello ^_^')


def passive():
    pass


def open_app(filename=None):
    database = Database.get_apps()
    # открытие приложения
    if filename is None:
        voice.speaker("произошла какая-то ошибка")
        return
    # filename = transliterate(filename, 'ru')
    filename = filename.replace(" ", "")
    max_correlation = 0
    best_filepath = ""
    best_filename = ""
    for name in database:
        print(filename, name, SequenceMatcher(None, name, filename).ratio())
        if SequenceMatcher(None, name, filename).ratio() > max_correlation:
            max_correlation = SequenceMatcher(None, name, filename).ratio()
            best_filename = name
            best_filepath = database[name]
    voice.speaker("Открываю приложение" + best_filename)
    os.startfile(best_filepath)

def neuro_answer():
    pass

def create_file(file_path="файлики/"):
    # создание файла по указанному пути
    if file_path is None:
        voice.speaker("Произошла ошибка: не указан путь файла")
        return
    try:
        path = Path(file_path)
        # path.parent.mkdir(parents=True, exist_ok=True)# создаем директории если их нет
        # path.touch(exist_ok=True)  # создаем файл если он не существует
        file = open(file_path+'new.txt',"w+")
        voice.speaker(f"Файл {path.name} успешно создан")
    except Exception as e:
        voice.speaker(f"Ошибка при создании файла: {str(e)}")


def speak_time():
        # Получаем текущее время
        now = datetime.datetime.now()

        # Форматируем время в удобный для чтения формат
        current_time = now.strftime("%H часов %M минут")

        # Возвращаем строку с текущим временем
        return voice.speaker(f"Текущее время: {current_time}")
