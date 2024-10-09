from curses.ascii import isdigit

from setuptools.wheel import Wheel

print('Добро пожаловать в калькулятор ИМТ!!!')
while True:
    try:
        height = int(input("ВВедите Ваш рост в сантиметрах "))
        break
    except ValueError:
        print("Пожалуйста ведите цифры")
while True:
    try:
        weight = int(input("Введите Ваш вес в килограмах "))
        break
    except ValueError:
        print("Пожалуйста введите цифры!")


def calculator(h, w):
    result = h/w
    return print(round(result, 2))

calculator(height, weight)



