# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def is_valid(x, y):
    if x <= 0 or y >= 0:
        print('Первое число должно быть положительным, а второе - отрицательным!')
        return False
    else:
        return True


def my_func_1(x, y):
    return x ** y


def my_func_2(x, y):
    result = 1
    for i in range(abs(y)):
        result = result * (1 / x)
    return result


try:
    num_1 = float(input('Введите действительное положительное число, которое будет возводиться в степень: '))
    num_2 = int(input('Введите целое отрицательные число, которое будет являться степенью предыдущего числа: '))
    if is_valid(num_1, num_2):
        print(f'Ответ, полученный через оператор **: {my_func_1(num_1, num_2)}')
        print(f'Ответ, полученный с использованием цикла: {my_func_2(num_1, num_2)}')
except ValueError:
    print('Нужно ввести числа! Второе число должно быть целым!')
