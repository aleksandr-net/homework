#!/usr/bin/python3.5

tarelki = int(input('Количество тарелок:'))
sredstvo = float(input('Количество средства:'))

if tarelki < 0:
    print('Некорректные данные')
if sredstvo < 0:
    print('Некорректные данные')
else:
    while sredstvo >= 0:
        sredstvo = sredstvo - 0.5
        tarelki = tarelki - 1
        if tarelki == 0 and sredstvo == 0:
            print('Все тарелки вымыты, моющее средство закончилось')
            break
        if sredstvo == 0 and tarelki > 0:
            print('Моющее средство закончилось. Осталось', tarelki, 'тарелок')
            break
        if sredstvo > 0 and tarelki == 0:
            print('Все тарелки вымыты. Осталось', sredstvo, 'ед. моющего средства')
            break
