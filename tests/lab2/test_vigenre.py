import unittest
from src.lab2.vigenre import encrypt_vigenere, decrypt_vigenere


class TestVigenereCipher(unittest.TestCase):

    def test_encrypt_with_key_a(self):
        """Тест шифрования с ключом 'A' (без изменений)"""
        self.assertEqual(encrypt_vigenere("PYTHON", "A"), "PYTHON")
        self.assertEqual(encrypt_vigenere("python", "a"), "python")

    def test_encrypt_uppercase(self):
        """Тест шифрования текста в верхнем регистре"""
        self.assertEqual(encrypt_vigenere("ATTACKATDAWN", "LEMON"), "LXFOPVEFRNHR")
        self.assertEqual(encrypt_vigenere("HELLO", "KEY"), "RIJVS")

    def test_encrypt_lowercase(self):
        """Тест шифрования текста в нижнем регистре"""
        self.assertEqual(encrypt_vigenere("attackatdawn", "lemon"), "lxfopvefrnhr")
        self.assertEqual(encrypt_vigenere("hello", "key"), "rijvs")

    def test_encrypt_with_numbers(self):
        """Тест шифрования с цифрами"""
        result = encrypt_vigenere("Hello123", "key")
        self.assertEqual(result, "Rijvs123")

    def test_encrypt_with_special_chars(self):
        """Тест шифрования со спецсимволами"""
        result = encrypt_vigenere("Hello, World!", "key")
        self.assertEqual(result, "Rijvs, Ambpb!")

    def test_encrypt_empty_string(self):
        """Тест шифрования пустой строки"""
        self.assertEqual(encrypt_vigenere("", "key"), "")

    def test_encrypt_short_key(self):
        """Тест с коротким ключом (повторение ключа)"""
        result = encrypt_vigenere("AAAAAAA", "AB")
        self.assertEqual(result, "ABABABA")

    def test_encrypt_long_key(self):
        """Тест с длинным ключом"""
        result = encrypt_vigenere("ABC", "VERYLONGKEY")
        self.assertEqual(result, "VFT")

    def test_decrypt_with_key_a(self):
        """Тест дешифрования с ключом 'A' (без изменений)"""
        self.assertEqual(decrypt_vigenere("PYTHON", "A"), "PYTHON")
        self.assertEqual(decrypt_vigenere("python", "a"), "python")

    def test_decrypt_uppercase(self):
        """Тест дешифрования текста в верхнем регистре"""
        self.assertEqual(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"), "ATTACKATDAWN")
        self.assertEqual(decrypt_vigenere("RIJVS", "KEY"), "HELLO")

    def test_decrypt_lowercase(self):
        """Тест дешифрования текста в нижнем регистре"""
        self.assertEqual(decrypt_vigenere("lxfopvefrnhr", "lemon"), "attackatdawn")
        self.assertEqual(decrypt_vigenere("rijvs", "key"), "hello")

    def test_decrypt_with_special_chars(self):
        """Тест дешифрования со спецсимволами"""
        result = decrypt_vigenere("Rijvs, Ambpb!", "key")
        self.assertEqual(result, "Hello, World!")

    def test_decrypt_empty_string(self):
        """Тест дешифрования пустой строки"""
        self.assertEqual(decrypt_vigenere("", "key"), "")


if __name__ == '__main__':
    unittest.main()