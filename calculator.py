# функция сложения
def adducation():
    num_1 = float(input('Введите число №1 для сложения: '))
    num_2 = float(input('Введите число №2 для сложения: '))
    print('Сложение: ', num_1, ' + ', num_2, ' = ', num_1 + num_2)

# функция вычитания
def subtraction():
    num_1 = float(input('Введите число №1 для вычитания: '))
    num_2 = float(input('Введите число №2 для вычитания: '))
    print('Вычитание: ', num_1, ' - ', num_2, ' = ', num_1 - num_2)

# функция умножения
def multiplication():
    num_1 = float(input('Введите число №1 для умножения: '))
    num_2 = float(input('Введите число №2 для умножения: '))
    print('Умножение: ', num_1, ' * ', num_2, ' = ', num_1 * num_2)

# функция деления
def division():
    num_1 = float(input('Введите число №1 для деления: '))
    num_2 = float(input('Введите число №2 для деления: '))
    # условие о том, что на 0 делить нельзя
    if num_2 != 0:
        print('Деление: ', num_1, ' / ', num_2, ' = ', num_1 / num_2)
    else:
        print('Ошибка: Деление на 0 невозможно!')

# сообщение для пользователя
print("Начало операций:")
# вывод функций
adducation()
subtraction()
multiplication()
division()

