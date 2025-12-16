import unittest
import os
import subprocess
import sys

USER_SCRIPT_NAME = r'C:\Users\user\PycharmProjects\proga\src\lab4\task.py'


class TestOrderProcessing(unittest.TestCase):

    def setUp(self):
        """
        Создаем тестовый файл orders.txt перед каждым тестом.
        Здесь мы моделируем разные ситуации:
        1. Валидный заказ (Россия, MAX)
        2. Валидный заказ (Другая страна, LOW)
        3. Ошибка в телефоне
        4. Ошибка в адресе (пустой)
        5. Ошибка в адресе (не хватает полей)
        6. Две ошибки сразу
        """
        self.test_data = [
            "10001;Яблоко, Груша, Яблоко;Иванов Иван;Россия. Область. Город. Улица;+7-900-000-00-00;MAX",
            "10002;Банан;Петров Петр;США. Штат. Город. Стрит;+1-200-000-00-00;LOW",
            "20001;Сок;Сидоров Сидор;Россия. Область. Город. Улица;+7-900-000-00;MIDDLE",  # Ошибка телефона (короткий)
            "30001;Хлеб;Пустой Адрес;;+7-900-000-00-00;LOW",  # Пустой адрес
            "30002;Сыр;Неполный Адрес;Россия. Москва;+7-900-000-00-00;LOW",  # Неполный адрес
            "40001;Вода;Две Ошибки;Нет Адреса;+0-000;MAX"  # Ошибка адреса и телефона
        ]

        with open('orders.txt', 'w', encoding='utf-8') as f:
            for line in self.test_data:
                f.write(line + '\n')

        # Удаляем выходные файлы, если они есть, чтобы тест был чистым
        if os.path.exists('non_valid_orders.txt'):
            os.remove('non_valid_orders.txt')
        if os.path.exists('order_country.txt'):
            os.remove('order_country.txt')

    def tearDown(self):
        """Удаляем созданные файлы после тестов (можно закомментировать для отладки)"""
        files_to_remove = ['orders.txt', 'non_valid_orders.txt', 'order_country.txt']
        for f in files_to_remove:
            if os.path.exists(f):
                os.remove(f)

    def run_user_script(self):
        """Запускает код пользователя как отдельный процесс"""
        result = subprocess.run([sys.executable, USER_SCRIPT_NAME], capture_output=True, text=True)
        # Проверяем, что скрипт выполнился без падения (код возврата 0)
        self.assertEqual(result.returncode, 0, f"Скрипт упал с ошибкой:\n{result.stderr}")

    def test_files_creation(self):
        """Проверка, что файлы создаются"""
        self.run_user_script()
        self.assertTrue(os.path.exists('non_valid_orders.txt'), "Файл non_valid_orders.txt не создан")
        self.assertTrue(os.path.exists('order_country.txt'), "Файл order_country.txt не создан")

    def test_non_valid_orders_content(self):
        """Проверка логики валидации ошибок"""
        self.run_user_script()

        with open('non_valid_orders.txt', 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]

        # Ожидаем увидеть ошибки для заказов 20001, 30001, 30002, 40001

        # Проверка ошибки телефона (Тип 2)
        phone_error = any("20001;2;+7-900-000-00" in line for line in lines)
        self.assertTrue(phone_error, "Не найдена или неверна запись об ошибке телефона (заказ 20001)")

        # Проверка пустого адреса (Тип 1) -> должно быть 'no data'
        empty_addr_error = any("30001;1;no data" in line for line in lines)
        self.assertTrue(empty_addr_error, "Не найдена обработка пустого адреса как 'no data' (заказ 30001)")

        # Проверка неполного адреса (Тип 1)
        partial_addr_error = any("30002;1;Россия. Москва" in line for line in lines)
        self.assertTrue(partial_addr_error, "Не найдена ошибка неверного формата адреса (заказ 30002)")

        # Проверка двойной ошибки (40001) - должно быть две записи
        double_error_addr = any("40001;1" in line for line in lines)
        double_error_phone = any("40001;2" in line for line in lines)
        self.assertTrue(double_error_addr and double_error_phone, "Для заказа 40001 должны быть записаны обе ошибки")

    def test_order_country_logic(self):
        """Проверка формата вывода валидных заказов и группировки продуктов"""
        self.run_user_script()

        with open('order_country.txt', 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]

        # Проверка количества валидных заказов (должно быть 2: 10001 и 10002)
        self.assertEqual(len(lines), 2, "В order_country.txt должно быть ровно 2 валидных заказа из тестового набора")

        # Проверка группировки продуктов (Яблоко x2)
        # Заказ 10001: Яблоко, Груша, Яблоко -> Яблоко x2, Груша (порядок может зависеть от реализации, проверяем наличие подстрок)
        row_10001 = next((line for line in lines if "10001" in line), None)
        self.assertIsNotNone(row_10001, "Заказ 10001 потерян")
        self.assertIn("Яблоко x2", row_10001, "Неверная группировка продуктов (ожидалось 'Яблоко x2')")

        # Проверка формата адреса в выводе (Без страны: Регион. Город. Улица)
        # Вход: Россия. Область. Город. Улица -> Выход: Область. Город. Улица
        self.assertIn("Область. Город. Улица", row_10001, "Адрес должен быть обрезан (без страны)")
        self.assertNotIn("Россия. Область", row_10001, "В выводе адреса не должно быть страны")

    def test_sorting_rules(self):
        """Проверка сортировки: Россия первая, потом по алфавиту"""
        # Переписываем setup для теста сортировки
        data = [
            "1;A;F;Англия. A. A. A;+7-900-000-00-00;LOW",
            "2;A;F;Россия. R. R. R;+7-900-000-00-00;LOW",
            "3;A;F;Германия. G. G. G;+7-900-000-00-00;LOW"
        ]
        with open('orders.txt', 'w', encoding='utf-8') as f:
            for line in data:
                f.write(line + '\n')

        self.run_user_script()

        with open('order_country.txt', 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]

        # Ожидаемый порядок: Россия (2), Англия (1), Германия (3) -> (Англия на А, Германия на Г)
        # Если сортировка по алфавиту стран: Англия, Германия. Россия должна быть исключена из алфавита и стоять первой.

        ids = [line.split(';')[0] for line in lines]
        self.assertEqual(ids[0], "2", "Первой должна идти Россия")
        # Дальше Англия (А) или Германия (Г). 'А' < 'Г'
        self.assertEqual(ids[1], "1", "Второй должна быть Англия (по алфавиту после спец. правила для РФ)")
        self.assertEqual(ids[2], "3", "Третьей должна быть Германия")


if __name__ == '__main__':
    unittest.main()