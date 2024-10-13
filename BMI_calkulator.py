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
    result = w/((h/100)**2)
    return round(result, 2)


person = calculator(height, weight)

if person < 18.5:
    print("Недостаточная масса тела !")
elif 18.5 == person < 24.9:
    print("Норма !!!")
elif 25 >= person < 29.9:
    print('Избыточная масса тела')
else:
    print("Ожирение !")






