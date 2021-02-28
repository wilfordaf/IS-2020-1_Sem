import numpy as np
import math
from PIL import Image  # подключаем необходимые библиотеки


def binary(n, number, lnght, arr):  # функция перевода десятичного числа в заднное по кол-ву бит двоичное
    s = ''
    for i in range(number):
        if arr[i] == 0:
            arr[i] = n
            break
        elif arr[i] == n:
            break
    a = (arr.index(n) % 6)
    if a == 0:
        s = "0" * lnght
        return s
    while a > 0:
        s = str(a % 2) + s
        a //= 2
    while len(s) < lnght:
        s = "0" + s
    return s


def shannon(n):
    if n == 100:
        return "1"
    elif n == 240:
        return "01"
    elif n == 20:
        return "010"
    elif n == 80:
        return "0110"
    elif n == 60:
        return "01110"
    elif n == 140:
        return "01111"


def haffman(n):
    if n == 100:
        return "0"
    elif n == 240:
        return "10"
    elif n == 20:
        return "101"
    elif n == 80:
        return "1001"
    elif n == 60:
        return "10001"
    elif n == 140:
        return "10000"


fout = open('report.txt', 'w')  # определяем вывод в файл report.txt

# 1 ЗАДАНИЕ
img = Image.open('digitalculture.png')  # открываем файл
# img.show()  # вывод картинки
arr = np.array(img)  # преобразование картинки в трёхмерный массив формата строка/столбец/градация серого

# 2 ЗАДАНИЕ
message = []  # создание массива
for i in range(128):
    message.append(arr[64][i][1])  # добавляем в массив message глубину серого в каждом пикселе
    message[i] = round(message[i] // 20) * 20  # применяем указанную формулу к элементу массива
print(message, file=fout)  # результат выводим в файл

# 3 ЗАДАНИЕ
frequency = [0] * 256  # массив для частоты каждой из градаций
for i in range(128):
    frequency[message[i]] += (1 / 128)  # подсчёт частоты символом с помощью сортировки подсчётом
frequency.sort()
frequency.reverse()  # сортировка массива частот по возрастанию
print(frequency, file=fout)  # результат выводим в файл

# 4 ЗАДАНИЕ
quantity = 0  # количество уникальных символов
minbitlength = 0  # минимальная длина битового представления цвета
enthropy = 0  # энтропия
for i in range(256):
    if frequency[i] != 0:
        quantity += 1  # подсчёт количества уникальных символов
        enthropy -= (frequency[i] * math.log2(frequency[i]))  # подсчёт энтропии по формуле
minbitlength = math.ceil((math.log2(quantity)))  # подсчёт минимальной длины в битах по формуле Шеннона
print(quantity, file=fout)
print(minbitlength, file=fout)
print(enthropy, file=fout)

# 8 ЗАДАНИЕ
equalbincodeout = [0] * 128
equalbincode = [0] * quantity
for i in range(128):
    equalbincodeout[i] = binary(message[i], quantity, minbitlength,
                                equalbincode)  # получение равномерного двоичного кода
print(equalbincodeout, file=fout)  # вывод сообщения записанного с помощью равномерного двоичного кода
amount = minbitlength * 128  # количество информации по формуле вес символа*количество символов
print(amount, file=fout)

# 9 ЗАДАНИЕ
cnt = 0
shannon_message = [0] * 128
for i in range(128):
    shannon_message[i] = shannon(message[i])
    cnt += len(shannon(message[i]))
print(shannon_message, file=fout)
print(cnt, ";", cnt / 128, file=fout)

# 10 ЗАДАНИЕ
cntr = 0
haffman_message = [0] * 128
for i in range(128):
    haffman_message[i] = haffman(message[i])
    cntr += len(haffman(message[i]))
print(haffman_message, file=fout)
print(cntr, ";", cntr / 128, file=fout)

# 11 ЗАДАНИЕ
information = 0
for i in range(quantity):
    information -= ((1/quantity) * math.log2((1/quantity)))
print(information, file=fout)
print(1-(enthropy/information),file=fout)
fout.close()
