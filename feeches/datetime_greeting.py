import datetime

def get_greeting():
    now = datetime.datetime.now()
    hour = now.hour
    if hour < 6:
        return "Доброй ночи"
    elif hour >= 6 and hour < 12:
        return "Доброе утро"
    elif hour >= 12 and hour < 18:
        return "Добрый день"
    else:
        return "Добрый вечер"

if __name__ == "__main__":
    greeting = get_greeting()
    print(f"Сейчас {greeting}")