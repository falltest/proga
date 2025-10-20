import unittest
from src.lab2.caesar import encrypt_caesar, decrypt_caesar


class TestCaesarCipher(unittest.TestCase):

    def test_encrypt_uppercase(self):
        """Тест шифрования текста в верхнем регистре"""
        self.assertEqual(encrypt_caesar("PYTHON"), "SBWKRQ")
        self.assertEqual(encrypt_caesar("HELLO"), "KHOOR")
        self.assertEqual(encrypt_caesar("ABC"), "DEF")

    def test_encrypt_lowercase(self):
        """Тест шифрования текста в нижнем регистре"""
        self.assertEqual(encrypt_caesar("python"), "sbwkrq")
        self.assertEqual(encrypt_caesar("hello"), "khoor")
        self.assertEqual(encrypt_caesar("abc"), "def")

    def test_encrypt_mixed_case(self):
        """Тест шифрования текста со смешанным регистром"""
        self.assertEqual(encrypt_caesar("Python3.6"), "Sbwkrq3.6")
        self.assertEqual(encrypt_caesar("HeLLo"), "KhOOr")

    def test_encrypt_empty_string(self):
        """Тест шифрования пустой строки"""
        self.assertEqual(encrypt_caesar(""), "")

    def test_encrypt_with_numbers(self):
        """Тест шифрования текста с цифрами"""
        self.assertEqual(encrypt_caesar("Test123"), "Whvw123")
        self.assertEqual(encrypt_caesar("2024"), "2024")

    def test_encrypt_with_special_chars(self):
        """Тест шифрования текста со спецсимволами"""
        self.assertEqual(encrypt_caesar("Hello, World!"), "Khoor, Zruog!")
        self.assertEqual(encrypt_caesar("a.b.c"), "d.e.f")

    def test_encrypt_custom_shift(self):
        """Тест шифрования с пользовательским сдвигом"""
        self.assertEqual(encrypt_caesar("ABC", 1), "BCD")
        self.assertEqual(encrypt_caesar("ABC", 5), "FGH")
        self.assertEqual(encrypt_caesar("XYZ", 3), "ABC")

    def test_decrypt_uppercase(self):
        """Тест дешифрования текста в верхнем регистре"""
        self.assertEqual(decrypt_caesar("SBWKRQ"), "PYTHON")
        self.assertEqual(decrypt_caesar("KHOOR"), "HELLO")

    def test_decrypt_lowercase(self):
        """Тест дешифрования текста в нижнем регистре"""
        self.assertEqual(decrypt_caesar("sbwkrq"), "python")
        self.assertEqual(decrypt_caesar("khoor"), "hello")

    def test_decrypt_mixed_case(self):
        """Тест дешифрования со смешанным регистром"""
        self.assertEqual(decrypt_caesar("Sbwkrq3.6"), "Python3.6")

    def test_decrypt_empty_string(self):
        """Тест дешифрования пустой строки"""
        self.assertEqual(decrypt_caesar(""), "")

    def test_decrypt_custom_shift(self):
        """Тест дешифрования с пользовательским сдвигом"""
        self.assertEqual(decrypt_caesar("BCD", 1), "ABC")
        self.assertEqual(decrypt_caesar("FGH", 5), "ABC")


if __name__ == '__main__':
    unittest.main(verbosity=2)