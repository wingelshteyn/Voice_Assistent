# import winapps
# import subprocess
#
# # get a list of installed apps
# installed_apps = winapps.list_installed()
#
# # create a dictionary of app names and their installation paths
# app_paths = {}
# for app in installed_apps:
#     app_paths[app.name.lower()] = app.install_location
#
# # use the dictionary to open apps with voice commands
# def open_app(app_name):
#     for i in app_paths:
#         if app_name in i:
#             app_path = app_paths[i]
#             subprocess.Popen([app_path])
#             print(i + " opened")
#             return
#     print(app_name + " is not installed")
#
# open_app('steam')
# ==================================================================
# import os
# import subprocess
#
# def run_prog(name):
#     """
#     Ищет исполняемый файл по частичному названию и запускает его.
#
#     Args:
#         частичное_название (str): Часть названия исполняемого файла.
#
#     Returns:
#         None
#     """
#
#     # Определение всех исполняемых файлов на компьютере
#     all_files = []
#     for root, directories, files in os.walk("C:\\"):
#         for file in files:
#             if file.endswith(".exe"):
#                 full_path = os.path.join(root, file)
#                 all_files.append(full_path)
#
#     # Поиск файлов, соответствующих частичному названию
#     founded_files = [file for file in all_files if name in file]
#
#     # Если найдено несколько файлов, предлагаем выбрать
#     if len(founded_files) > 1:
#         print("Найдено несколько файлов, соответствующих частичному названию:")
#         for i, file in enumerate(founded_files):
#             print(f"{i + 1}. {file}")
#
#         choise =  int(input("Введите номер файла для запуска: ")) - 1
#         if 0 <= choise < len(founded_files):
#             choosen_file = founded_files[choise]
#         else:
#             print("Неверный номер.")
#             return
#     elif len(founded_files) == 1:
#         choosen_file = founded_files[0]
#     else:
#         print(f"Файл с частичным названием '{name}' не найден.")
#         return
#
#     # Запуск программы
#     print(f"Запускаю: {choosen_file}")
#     subprocess.run([choosen_file])
#
# # Пример использования
# run_prog("steam")
# ================================================================

from selenium.webdriver.common.by import By

def reg():
    try:
        driver = webdriver.Firefox()
        driver.maximize_window()

        # get lambdatest
        driver.get("https://e.sfu-kras.ru/")

        # get element
        driver.find_element(By.ID, "username").send_keys("KBudanov-KI23")
        driver.find_element(By.ID, "password").send_keys("R3pTqN282VPCaw6")
        driver.find_element(By.ID, "loginbtn").click()
    except:
        pass

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class YoutubeBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.youtube.com")

    def search_video(self, query):
        search_box = self.driver.find_element(By.NAME, "search_query")
        search_box.send_keys(query)
        search_box.submit()

    def pause_video(self):
        try:
            play_button = self.driver.find_element(By.CLASS_NAME, "ytp-play-button.ytp-button")
            play_button.click()
        except:
            print("Видео не воспроизводится.")

    def resume_video(self):
        try:
            pause_button = self.driver.find_element(By.XPATH, "//button[@aria-label='Pause']")
            pause_button.click()
        except :
            print("Видео уже воспроизводится.")

    def increase_volume(self):
        try:
            volume_slider = self.driver.find_element(By.CLASS_NAME, "ytp-volume-slider")
            current_volume = volume_slider.get_attribute("aria-valuenow")
            volume_slider.click()
            new_volume = int(current_volume) + 10
            if new_volume > 100:
                new_volume = 100
            self.driver.execute_script(f"arguments[0].setAttribute('aria-valuenow', {new_volume});", volume_slider)
        except :
            print("Не удалось найти ползунок громкости.")

    def decrease_volume(self):
        try:
            volume_slider = self.driver.find_element(By.CLASS_NAME, "ytp-volume-slider")
            current_volume = volume_slider.get_attribute("aria-valuenow")
            volume_slider.click()
            new_volume = int(current_volume) - 10
            if new_volume < 0:
                new_volume = 0
            self.driver.execute_script(f"arguments[0].setAttribute('aria-valuenow', {new_volume});", volume_slider)
        except :
            print("Не удалось найти ползунок громкости.")

    def fullscreen(self):
        try:
            fullscreen_button = self.driver.find_element(By.CLASS_NAME, "ytp-fullscreen-button.ytp-button")
            fullscreen_button.click()
        except :
            print("Не удалось найти кнопку полноэкранного режима.")

    def like_video(self):
        try:
            like_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//yt-icon[@id='like-button']"))
            )
            like_button.click()
        except :
            print("Не удалось найти кнопку лайка.")

    def dislike_video(self):
        try:
            dislike_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//yt-icon[@id='dislike-button']"))
            )
            dislike_button.click()
        except :
            print("Не удалось найти кнопку дизлайка.")

    def close(self):
        self.driver.quit()

# bot = YoutubeBot()
# bot.search_video("Как сделать сайт")
# input()
# bot.like_video()
# bot.increase_volume()
# # bot.fullscreen()
# bot.pause_video()


#
# driver = webdriver.Firefox()
# driver.get("https://alice.yandex.ru/?npr=2")
#
# driver.find_element(By.CLASS_NAME, "input-container__text-input svelte-223isq").send_keys("придумай анекдот")
# driver.find_element(By.CLASS_NAME, "yamb-oknyx__arrow-circle").click()
# print(driver.find_element(By.CLASS_NAME, "markdown-text markdown-text_standalone").text)