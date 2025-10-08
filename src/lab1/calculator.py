import math


class Calculator:
    """Простой калькулятор с основными математическими операциями"""

    @staticmethod
    def add(first_number, second_number):
        """Сложение"""
        return first_number + second_number

    @staticmethod
    def subtract(first_number, second_number):
        """Вычитание"""
        return first_number - second_number

    @staticmethod
    def multiply(first_number, second_number):
        """Умножение"""
        return first_number * second_number

    @staticmethod
    def divide(first_number, second_number):
        """Деление
        Выдает ошибку, если пользователь хотел поделить на 0"""
        if second_number == 0:
            raise ValueError("Деление на ноль невозможно!")
        return first_number / second_number

    @staticmethod
    def power(first_number, second_number):
        """Возведение в степень"""
        return first_number ** second_number

    @staticmethod
    def sqrt(first_number):
        """Квадратный корень
        Выдает ошибку, если введено отрицательное число"""
        if first_number < 0:
            raise ValueError("Нельзя извлечь корень из отрицательного числа!")
        return math.sqrt(first_number)

    @staticmethod
    def percent(first_number, second_number):
        """Процент от числа (b% от a)"""
        return (first_number * second_number) / 100


def main():
    """Главная функция для работы калькулятора через терминал"""
    calc = Calculator()

    print("=" * 50)
    print("КАЛЬКУЛЯТОР")
    print("=" * 50)

    while True:
        print("\nДоступные операции:")
        print("1. Сложение (+)")
        print("2. Вычитание (-)")
        print("3. Умножение (*)")
        print("4. Деление (/)")
        print("5. Возведение в степень (^)")
        print("6. Квадратный корень (√)")
        print("7. Процент (%)")
        print("0. Выход")

        choice = input("\nВыберите операцию (0-7): ").strip()

        if choice == "0":
            print("Выход из программы. До свидания!")
            break

        try:
            if choice == "6":  # Квадратный корень требует только одно число
                num = float(input("Введите число: "))
                result = calc.sqrt(num)
                print(f"\n√{num} = {result}")

            elif choice in ["1", "2", "3", "4", "5", "7"]:
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))

                if choice == "1":
                    result = calc.add(num1, num2)
                    print(f"\n{num1} + {num2} = {result}")

                elif choice == "2":
                    result = calc.subtract(num1, num2)
                    print(f"\n{num1} - {num2} = {result}")

                elif choice == "3":
                    result = calc.multiply(num1, num2)
                    print(f"\n{num1} * {num2} = {result}")

                elif choice == "4":
                    result = calc.divide(num1, num2)
                    print(f"\n{num1} / {num2} = {result}")

                elif choice == "5":
                    result = calc.power(num1, num2)
                    print(f"\n{num1} ^ {num2} = {result}")

                elif choice == "7":
                    result = calc.percent(num1, num2)
                    print(f"\n{num2}% от {num1} = {result}")

            else:
                print("\nОшибка! Выберите корректную операцию.")

        except ValueError as e:
            print(f"\nОшибка: {e}")
        except Exception as e:
            print(f"\nПроизошла ошибка: {e}")


if __name__ == "__main__":
    main()
