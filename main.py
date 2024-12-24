import math

# Константа для количества итераций
ITERATIONS = 10


def cos_series(x):
    """
    Вычисляет косинус числа x с использованием разложения в ряд Тейлора.

    Короткое описание:
    Реализация разложения cos(x) = 1 - x^2/2! + x^4/4! - ... для заданного числа итераций.

    Описание:
    Функция использует цикл для вычисления суммы ряда Тейлора для cos(x).
    Количество итераций задается константой ITERATIONS.

    Аргументы:
    x (float): Число, для которого нужно вычислить cos(x).

    Возвращаемое значение:
    float: Приблизительное значение cos(x).

    Исключения:
    ValueError: Если x не является числом.

    Примеры использования:
    >>> cos_series(0)
    1.0
    >>> cos_series(math.pi / 3)
    0.5000000000
    """
    if not isinstance(x, (int, float)):
        raise ValueError("x должен быть числом")

    result = 0
    for n in range(ITERATIONS):
        term = ((-1) ** n) * (x ** (2 * n)) / math.factorial(2 * n)
        result += term
    return result


def ln_series(x):
    pass


def main():
    """
    Главное меню программы.

    Описание:
    Пользователь выбирает функцию (cos(x) или ln(1-x)), вводит значение x,
    и получает результат на экран.
    """
    while True:
        print("\nМеню:"
              "\n1. Вычислить cos(x)"
              "\n2. Вычислить ln(1-x)"
              "\n3. Выйти")
        choice = input("\nВведите ваш выбор (1/2/3): ")

        if choice == "1":
            try:
                x = float(input("Введите значение x: "))
                print(f"cos({x}) ≈ {cos_series(x)}")
            except ValueError as e:
                print(f"Ошибка: {e}")
        elif choice == "2":
            try:
                x = float(input("Введите значение x (в пределах -1 < x <= 1): "))
                print(f"ln(1-{x}) ≈ {ln_series(x)}")
            except ValueError as e:
                print(f"Ошибка: {e}")
        elif choice == "3":
            print("Выход из программы. До свидания!")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
