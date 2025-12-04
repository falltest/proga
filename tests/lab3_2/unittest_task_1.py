import unittest
import subprocess
import sys
import os

PROJECT_DIR = r'C:\Users\user\PycharmProjects\proga\src\lab3_2'

SCRIPT_NAME = 'task_1.py'
OUTPUT_FILE = 'output.txt'

FILMS_FILE = 'input_films.txt'
PEOPLE_FILE = 'input_people.txt'
USER_INPUT_FILE = 'input.txt'


class TestMovieRecommendation(unittest.TestCase):

    def setUp(self):
        """Подготовка путей"""
        self.output_path = os.path.join(PROJECT_DIR, OUTPUT_FILE)
        self.films_path = os.path.join(PROJECT_DIR, FILMS_FILE)
        self.people_path = os.path.join(PROJECT_DIR, PEOPLE_FILE)
        self.user_input_path = os.path.join(PROJECT_DIR, USER_INPUT_FILE)

    def create_data(self, films_content, people_content, user_input_content):
        """Вспомогательная функция для создания всех 3 файлов"""
        with open(self.films_path, 'w', encoding='utf-8') as f:
            f.write(films_content)
        with open(self.people_path, 'w', encoding='utf-8') as f:
            f.write(people_content)
        with open(self.user_input_path, 'w', encoding='utf-8') as f:
            f.write(user_input_content)

    def run_script(self):
        """Запуск твоего скрипта"""
        subprocess.run([sys.executable, SCRIPT_NAME], cwd=PROJECT_DIR, check=True)

    def get_result(self):
        """Чтение результата"""
        if not os.path.exists(self.output_path):
            return ""
        with open(self.output_path, 'r', encoding='utf-8') as f:
            return f.read().strip()

    # --- ТЕСТ 1: Пример из задания ---
    def test_example_dune(self):
        films = """1,Мстители: Финал
2,Хатико
3,Дюна
4,Унесенные призраками"""

        people = """2,1,3
1,4,3
2,2,2,2,2,3"""

        user_in = "2,4"

        self.create_data(films, people, user_in)
        self.run_script()

        self.assertEqual(self.get_result(), "Дюна")

    # --- ТЕСТ 2: Битва популярности ---
    def test_popularity_logic(self):
        films = """10,Базовый фильм
20,Фильм А (Мало просмотров)
30,Фильм Б (Суперхит)"""

        people = """10,20
10,30
30,30,30,30,30"""

        user_in = "10"

        self.create_data(films, people, user_in)
        self.run_script()

        self.assertEqual(self.get_result(), "Фильм Б (Суперхит)")

    def test_already_watched(self):
        films = """1,Кино 1
2,Кино 2"""

        people = """1,2"""

        user_in = "1,2"

        self.create_data(films, people, user_in)
        self.run_script()

        self.assertEqual(self.get_result(), "")


if __name__ == '__main__':
    unittest.main()