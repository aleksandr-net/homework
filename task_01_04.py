#!/usr/bin/python3.5

print('Введите координаты трёх точек\n')

AX = int(input('AX = '))
AY = int(input('AY = '))
BX = int(input('BX = '))
BY = int(input('BY = '))
CX = int(input('CX = '))
CY = int(input('CY = '))

# Вычислим длины сторон треугольника
AB = ((AX - BX) ** 2 + (AY - BY) ** 2) ** 0.5
BC = ((BX - CX) ** 2 + (BY - CY) ** 2) ** 0.5
AC = ((AX - CX) ** 2 + (AY - CY) ** 2) ** 0.5

# Выполним проверку, является ли треугольник прямоугольным
if AB ** 2 == BC ** 2 + AC ** 2:
    print('Прямоугольный')
elif BC ** 2 == AB ** 2 + AC ** 2:
    print('Прямоугольный')
elif AC ** 2 == AB ** 2 + BC ** 2:
    print('Прямоугольный')
else:
    print('Не прямоугольный')
