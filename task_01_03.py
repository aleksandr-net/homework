#!/usr/bin/python3.5

print('Введите три целых числа:\n')

a = int(input('Первое число:' ))
b = int(input('Второе число:' ))
c = int(input('Третье число:' ))
lst = [a, b, c]
n = 0

while n < len(lst):
    for i in range(0, len(lst) - 1):
        if lst[i] > lst[i + 1]:
            temp = lst[i + 1]
            lst[i + 1] = lst[i]
            lst[i] = temp
        n += 1

print(lst[0], ',', lst[1], ',', lst[2])
