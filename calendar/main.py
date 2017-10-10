#!/usr/bin/python3.5

print('\nЕжедневник. Выберите действие:\n')

print('1. Вывести список задач')
print('2. Добавить задачу')
print('3. Отредактировать задачу')
print('4. Завершить задачу')
print('5. Начать задачу сначала')
print('6. Выход\n')

chosen = input('Введите число: ')

if str(chosen).isdigit() and int(chosen) >= 1 and int(chosen) <= 6:
    print('YEEEE!')
else:
    print('NO-NO-NO! You wrong!')
