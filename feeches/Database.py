import os
import win32com.client
from silero_tts.silero_tts import transliterate


class Database:

    @staticmethod
    def get_apps():

        def resolve_shortcut(shortcut_path):
            if shortcut_path.lower().endswith((".lnk", ".url")):
                shell = win32com.client.Dispatch("WScript.Shell")
                shortcut = shell.CreateShortcut(shortcut_path)
                target_path = os.path.abspath(shortcut.TargetPath)
                _, extension = os.path.splitext(target_path)

                # Исключаем unins000.exe, Uninstall.exe, setup.exe из выдачи
                if extension.lower() == ".exe" and os.path.basename(target_path).lower() not in (
                 "unins000.exe", "uninstall.exe", "setup.exe"):
                    return target_path
            return None

        def get_programs_from_start_menu():
            start_menu_path = os.path.join(os.environ['ProgramData'], 'Microsoft', 'Windows', 'Start Menu', 'Programs')

            programs = []

            for root, dirs, files in os.walk(start_menu_path):
                for file in files:
                    program_path = os.path.join(root, file)
                    programs.append(program_path)

            return programs

            # Пример использования
        programs = get_programs_from_start_menu()
        database = {}
        for program in programs:
            exe_path = resolve_shortcut(program)
            if exe_path is not None:
                # print(f"Ярлык: {program}, Путь к .exe: {exe_path}")
                database[transliterate(program.split("\\")[-1].split(".")[0].split(" ")[0], 'en')] = exe_path
        return database
