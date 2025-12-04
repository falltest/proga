import unittest
import subprocess
import sys
import os

PROJECT_DIR = r'C:\Users\user\PycharmProjects\proga\src\lab3_2'

SCRIPT_NAME = 'task_2.py'
OUTPUT_FILE = 'output.txt'
PEOPLE_FILE = 'people.txt'
VOZRAST_FILE = 'vozrast.txt'


class TestAgeGroups(unittest.TestCase):

    def setUp(self):
        """Подготовка путей к файлам"""
        self.output_path = os.path.join(PROJECT_DIR, OUTPUT_FILE)
        self.people_path = os.path.join(PROJECT_DIR, PEOPLE_FILE)
        self.vozrast_path = os.path.join(PROJECT_DIR, VOZRAST_FILE)

    def run_script(self):
        subprocess.run([sys.executable, SCRIPT_NAME], cwd=PROJECT_DIR, check=True)

    def verify_output(self, expected_text):
        """Считываем output.txt и сверяем с ожидаемым текстом"""
        with open(self.output_path, 'r', encoding='utf-8') as f:
            result = f.read().strip()

        result = result.replace('\r\n', '\n')
        expected_text = expected_text.replace('\r\n', '\n')

        self.assertEqual(result, expected_text)

    def test_official_example(self):
        with open(self.vozrast_path, 'w', encoding='utf-8') as f:
            f.write("18 25 35 45 60 80 100")

        with open(self.people_path, 'w', encoding='utf-8') as f:
            f.write("Кошельков Захар Брониславович,105\n")
            f.write("Дьячков Нисон Иринеевич,88\n")
            f.write("Иванов Варлам Якунович,88\n")
            f.write("Старостин Ростислав Ермолаевич,50\n")
            f.write("Ярилова Розалия Трофимовна,29\n")
            f.write("Соколов Андрей Сергеевич,15\n")
            f.write("Егоров Алан Петрович,7")

        self.run_script()

        expected = """101+: Кошельков Захар Брониславович (105)
81-100: Дьячков Нисон Иринеевич (88), Иванов Варлам Якунович (88)
46-60: Старостин Ростислав Ермолаевич (50)
26-35: Ярилова Розалия Трофимовна (29)
0-18: Соколов Андрей Сергеевич (15), Егоров Алан Петрович (7)"""

        self.verify_output(expected)

    def test_boundaries_and_sorting(self):
        with open(self.vozrast_path, 'w', encoding='utf-8') as f:
            f.write("10 20")

        with open(self.people_path, 'w', encoding='utf-8') as f:
            f.write("Алексеев Алексей,10\n")
            f.write("Борисов Борис,11\n")
            f.write("Викторов Виктор,21\n")
            f.write("Андреев Андрей,10")

        self.run_script()

        expected = """21+: Викторов Виктор (21)
11-20: Борисов Борис (11)
0-10: Алексеев Алексей (10), Андреев Андрей (10)"""

        self.verify_output(expected)


if __name__ == '__main__':
    unittest.main()