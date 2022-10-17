# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# from random import *
# n = int(input("Введите размер списка: "))
# some_list = [randint(-n, n) for _ in range(n)]
# print(some_list)
# sum = 0
# for i in range(len(some_list)):
#     if i % 2 != 0:
#         sum += some_list[i]
# print(sum)

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# n = int(input("Введите размер списка: "))
# some_list = [randint(-n, n) for _ in range(n)]
# print(some_list)
# some_list2 = []

# Первый способ:

# ind = 0
# while ind < len(some_list) / 2:
#     a = some_list[ind] * some_list[len(some_list) - ind - 1]
#     some_list2.append(a)
#     ind += 1
# print(some_list2)

# Второй способ:

# if len(some_list) % 2 != 0:
#     for i in range(len(some_list) // 2 + 1):
#         a = some_list[i] * some_list[len(some_list) - i - 1]
#         some_list2.append(a)
# elif len(some_list) % 2 == 0:
#     for i in range(len(some_list) // 2):
#         a = some_list[i] * some_list[len(some_list) - i - 1]
#         some_list2.append(a)
# else:
#     print('error')
# print(some_list2)

# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# n, m, r = int(input('Диапазон от: ')), int(input('Диапазон до: ')), int(input('Размер списка: '))
# some_list = [round(uniform(n, m), 2) for _ in range(r)]
# print(some_list)
# max, min = some_list[0] % 1, some_list[0] % 1
# for i in some_list:
#     if i % 1 > max:
#         max = round(i % 1, 2)
# print(max)
# for j in some_list:
#     if j % 1 < min:
#         min = round(j % 1, 2)
# print(min)
# diff = round(max, 2) - round(min, 2)
# print(f'Разница между максимальным и минимальным значением дробной части элементов = {diff}.')

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# number = int(input())

# binary_number = ''

# while number > 0:
#     binary_number = str(number % 2) + binary_number
#     number //= 2
# print(binary_number)
# print(bin(45))

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# n = int(input('Введите число: '))

# nega_fibonacci = []
# a, b = 1, 1
# for i in range(n):
#     nega_fibonacci.append(a)
#     a, b = b, a + b
# a, b = 0, 1
# for i in range(n + 1):
#     nega_fibonacci.insert(0, a)
#     a, b = b, a - b

# print(nega_fibonacci)

# ДОП Задача:
# Ввод: ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
# Вывод: [['ate', 'eat', 'tea'], ['nat', 'tan'], ['bat']]
# т.е сгруппировать слова по "общим букам".
# from collections import defaultdict

# some_list = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
# grups = defaultdict(list)
# for i in some_list:
#     k = sorted(i)
#     grups[tuple(k)].append(i)
    
# print([sorted(some_list) for some_list in grups.values()])








