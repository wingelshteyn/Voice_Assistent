# Импортируем необходимые модули
import socket
import subprocess

# Функция для проверки подключения к Интернету
def check_internet_connection():
    try:
        # Подключаемся к сайту через HTTP
        response = subprocess.check_output(["curl", "-Is", "https://www.google.com"])
        return True
    except:
        return False

# Функция для проверки состояния Wi-Fi
def check_wifi_state():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Пытаемся установить соединение с портом 80 на localhost
        # Если соединение установлено, Wi-Fi включен
        s.connect(("8.8.8.8", 80))
        return True
    except:
        return False

# Функция для включения Wi-Fi, если он выключен
def enable_wifi():
    """Включает Wi-Fi на Windows."""
    try:
        # Используем команду netsh для управления сетевыми настройками
        subprocess.run(["netsh", "wlan", "set", "interface", "name=\"Wi-Fi\"", "enabled=true"], check=True)
        print("Wi-Fi успешно включен.")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при включении Wi-Fi: {e}")

import subprocess

def connect_to_wifi(ssid, password):
    """
    Функция для подключения к Wi-Fi сети.

    Args:
        ssid (str): Имя Wi-Fi сети.
        password (str): Пароль Wi-Fi сети.
    """

    # Заменяем эту строку на команду для вашей операционной системы.
    command = f"netsh wlan connect name=\"{ssid}\" ssid=\"{ssid}\" password=\"{password}\""

    # Выполняем команду в командной строке.
    subprocess.run(command, shell=True)

    # Пример использования
    connect_to_wifi("Название_сети", "Пароль")

# Основная программа
if __name__ == "__main__":
    # Проверяем подключение к Интернету
    if not check_internet_connection():
        # Проверяем состояние Wi-Fi
        if not check_wifi_state():
            # Включаем Wi-Fi
            enable_wifi()
        else:
            print("Wi-Fi включен, но нет подключения к Интернету")
    else:
        print("Подключён к Интернету")