import unittest
from src.lab2.rsa import (
    is_prime,
    gcd,
    multiplicative_inverse,
    generate_keypair,
    encrypt,
    decrypt
)


class TestRSA(unittest.TestCase):
    """Тесты для RSA"""

    # === Тесты is_prime (3 теста) ===

    def test_is_prime_true(self):
        """Проверка простых чисел"""
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(17))

    def test_is_prime_false(self):
        """Проверка составных чисел"""
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(1))

    # === Тесты gcd (2 теста) ===

    def test_gcd_basic(self):
        """НОД базовые случаи"""
        self.assertEqual(gcd(12, 15), 3)
        self.assertEqual(gcd(3, 7), 1)

    # === Тесты multiplicative_inverse (1 тест) ===

    def test_multiplicative_inverse(self):
        """Модульное обратное"""
        self.assertEqual(multiplicative_inverse(7, 40), 23)

    # === Тесты generate_keypair (3 теста) ===

    def test_generate_keypair_basic(self):
        """Генерация ключей"""
        public, private = generate_keypair(17, 19)

        self.assertIsInstance(public, tuple)
        self.assertIsInstance(private, tuple)
        self.assertEqual(len(public), 2)
        self.assertEqual(len(private), 2)

    def test_generate_keypair_non_prime_error(self):
        """Ошибка при не простых числах"""
        with self.assertRaises(ValueError):
            generate_keypair(4, 7)

    def test_generate_keypair_equal_primes_error(self):
        """Ошибка при p = q"""
        with self.assertRaises(ValueError):
            generate_keypair(7, 7)

    # === Тесты encrypt/decrypt (6 тестов) ===

    def test_encrypt_simple(self):
        """Простое шифрование"""
        public, private = generate_keypair(61, 53)
        encrypted = encrypt(private, "HELLO")

        self.assertIsInstance(encrypted, list)
        self.assertEqual(len(encrypted), 5)

    def test_decrypt_simple(self):
        """Простая расшифровка"""
        public, private = generate_keypair(61, 53)
        encrypted = encrypt(private, "A")
        decrypted = decrypt(public, encrypted)

        self.assertEqual(decrypted, "A")

    def test_encrypt_empty_string(self):
        """Шифрование пустой строки"""
        public, private = generate_keypair(61, 53)
        encrypted = encrypt(private, "")

        self.assertEqual(encrypted, [])


if __name__ == '__main__':
    unittest.main(verbosity=2)