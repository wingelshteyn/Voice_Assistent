import re
from words2numsrus import NumberExtractor
import words

def random_range_parametrs(text):
    extractor = NumberExtractor()
    text = (extractor.replace_groups(text))
    print(text)
    try:
        match = re.search(r"от (\d+) до (\d+)", text)
        if match:
            return int(match.group(1)), int(match.group(2))
    except:
        return None


def youtube_query(text):
    try:
        text = re.sub("про |о том ", '', text)
        text = re.sub("ютубе|ютубчик", 'ютуб', text)
        match = re.search(r"(ютуб|видео) (.*)", text)
        if match:
            return f'"{match.group(2)}"'
    except:
        return None


def open_app_query(text):
    try:
        text = re.sub("запуск|запусти|запускай|открой", "", text)
        text = re.sub("приложение|программу|программа|проявление|приложения|переложение|переложения", 'utility', text)
        match = re.search(r"(utility) (.*)", text)
        if match:
            return f'"{match.group(2)}"'
    except:
        return None

def timer_parametr(text):
    extractor = NumberExtractor()
    text = (extractor.replace_groups(text))
    print(text)
    try:
        match = re.search(r"(\d+) (\w+)", text)
        if match:
            mult = 1
            if 'мин' in match.group(2):
                mult = 60
            if 'час' in match.group(2):
                mult = 3600
            print(int(match.group(1)), match.group(2))
            return int(match.group(1))*mult, match.group(2)
    except:
        return None


def count_parametrs(text):
    name = ''
    for e in words.TRIGGERS:
        name = e
        break
    text = re.sub(f"{name}|посчитай|сколько|будет|сколько будет|вычисли", "", text)
    text = re.sub("выражение|уравнение|проявление|приложения|переложение|переложения", "", text)
    extractor = NumberExtractor()
    text = (extractor.replace_groups(text))
    text = text.replace('икс', 'x')
    text = text.replace('игрек', 'y')
    text = text.replace('минус', '-')
    text = text.replace('плюс', '+')
    text = text.replace('умножить', '*')
    text = text.replace('разделить', '/')
    text = text.replace('равно', '=')
    text = text.replace('на', '')
    text = text.replace(' ', '')
    print(text)
    return f'"{text}"'
