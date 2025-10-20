import unittest
import math
from src.lab1.calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Тесты для калькулятора"""

    def setUp(self):
        """Подготовка перед каждым тестом"""
        self.calc = Calculator()

    # Тесты сложения
    def test_add_positive_numbers(self):
        """Тест сложения положительных чисел"""
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(10, 20), 30)

    def test_add_negative_numbers(self):
        """Тест сложения отрицательных чисел"""
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(-10, 5), -5)

    def test_add_floats(self):
        """Тест сложения дробных чисел"""
        self.assertAlmostEqual(self.calc.add(2.5, 3.7), 6.2)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3)

    def test_add_zero(self):
        """Тест сложения с нулем"""
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, 0), 0)

    # Тесты вычитания
    def test_subtract_positive_numbers(self):
        """Тест вычитания положительных чисел"""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(20, 15), 5)

    def test_subtract_negative_numbers(self):
        """Тест вычитания с отрицательными числами"""
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(10, -5), 15)

    def test_subtract_result_negative(self):
        """Тест вычитания с отрицательным результатом"""
        self.assertEqual(self.calc.subtract(5, 10), -5)

    # Тесты умножения
    def test_multiply_positive_numbers(self):
        """Тест умножения положительных чисел"""
        self.assertEqual(self.calc.multiply(5, 3), 15)
        self.assertEqual(self.calc.multiply(10, 10), 100)

    def test_multiply_negative_numbers(self):
        """Тест умножения с отрицательными числами"""
        self.assertEqual(self.calc.multiply(-5, 3), -15)
        self.assertEqual(self.calc.multiply(-5, -3), 15)

    def test_multiply_by_zero(self):
        """Тест умножения на ноль"""
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 10), 0)

    def test_multiply_floats(self):
        """Тест умножения дробных чисел"""
        self.assertAlmostEqual(self.calc.multiply(2.5, 4), 10.0)
        self.assertAlmostEqual(self.calc.multiply(0.5, 0.5), 0.25)

    # Тесты деления
    def test_divide_positive_numbers(self):
        """Тест деления положительных чисел"""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(20, 4), 5)

    def test_divide_negative_numbers(self):
        """Тест деления с отрицательными числами"""
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(-10, -2), 5)

    def test_divide_floats(self):
        """Тест деления дробных чисел"""
        self.assertAlmostEqual(self.calc.divide(7.5, 2.5), 3.0)
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.333333, places=5)

    def test_divide_by_zero(self):
        """Тест деления на ноль (должно вызвать исключение)"""
        with self.assertRaises(ValueError) as context:
            self.calc.divide(10, 0)
        self.assertIn("Деление на ноль", str(context.exception))

    def test_divide_zero_by_number(self):
        """Тест деления нуля на число"""
        self.assertEqual(self.calc.divide(0, 5), 0)

    # Тесты возведения в степень
    def test_power_positive_numbers(self):
        """Тест возведения в степень"""
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 2), 25)

    def test_power_zero_exponent(self):
        """Тест возведения в нулевую степень"""
        self.assertEqual(self.calc.power(5, 0), 1)
        self.assertEqual(self.calc.power(100, 0), 1)

    def test_power_negative_exponent(self):
        """Тест возведения в отрицательную степень"""
        self.assertEqual(self.calc.power(2, -1), 0.5)
        self.assertAlmostEqual(self.calc.power(10, -2), 0.01)

    def test_power_fractional_exponent(self):
        """Тест возведения в дробную степень"""
        self.assertAlmostEqual(self.calc.power(4, 0.5), 2.0)
        self.assertAlmostEqual(self.calc.power(27, 1 / 3), 3.0)

    # Тесты квадратного корня
    def test_sqrt_positive_numbers(self):
        """Тест квадратного корня из положительных чисел"""
        self.assertEqual(self.calc.sqrt(4), 2)
        self.assertEqual(self.calc.sqrt(9), 3)
        self.assertAlmostEqual(self.calc.sqrt(2), 1.414213, places=5)

    def test_sqrt_zero(self):
        """Тест квадратного корня из нуля"""
        self.assertEqual(self.calc.sqrt(0), 0)

    def test_sqrt_negative_number(self):
        """Тест квадратного корня из отрицательного числа (должно вызвать исключение)"""
        with self.assertRaises(ValueError) as context:
            self.calc.sqrt(-4)
        self.assertIn("отрицательного числа", str(context.exception))

    # Тесты процентов
    def test_percent_basic(self):
        """Тест вычисления процентов"""
        self.assertEqual(self.calc.percent(100, 10), 10)
        self.assertEqual(self.calc.percent(200, 50), 100)

    def test_percent_fractional(self):
        """Тест вычисления дробных процентов"""
        self.assertAlmostEqual(self.calc.percent(150, 33.33), 49.995)
        self.assertEqual(self.calc.percent(80, 25), 20)

    def test_percent_zero(self):
        """Тест вычисления нулевых процентов"""
        self.assertEqual(self.calc.percent(100, 0), 0)
        self.assertEqual(self.calc.percent(0, 50), 0)

    def test_percent_over_hundred(self):
        """Тест вычисления процентов больше 100"""
        self.assertEqual(self.calc.percent(50, 200), 100)


class TestCalculatorEdgeCases(unittest.TestCase):
    """Тесты граничных случаев"""

    def setUp(self):
        self.calc = Calculator()

    def test_very_large_numbers(self):
        """Тест с очень большими числами"""
        self.assertEqual(self.calc.add(10 ** 10, 10 ** 10), 2 * 10 ** 10)
        self.assertEqual(self.calc.multiply(10 ** 5, 10 ** 5), 10 ** 10)

    def test_very_small_numbers(self):
        """Тест с очень маленькими числами"""
        self.assertAlmostEqual(self.calc.add(0.000001, 0.000001), 0.000002)
        self.assertAlmostEqual(self.calc.multiply(0.0001, 0.0001), 0.00000001)

    def test_mixed_operations(self):
        """Тест комбинации операций"""
        result = self.calc.add(10, 5)
        result = self.calc.multiply(result, 2)
        result = self.calc.divide(result, 3)
        self.assertEqual(result, 10)


if __name__ == '__main__':
    # Запуск тестов с подробным выводом
    unittest.main(verbosity=2)