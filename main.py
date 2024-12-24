import math

def cos_series(x):
    pass


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
