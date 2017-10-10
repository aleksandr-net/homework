#!/usr/bin/python3.5

# Проверка, является ли элемент числом
def is_number(number):
    try:
        float(number)
        return True
    except ValueError:
        return False

# Общая функция для перевода в десятичную СС
def to_dec(system, number):
    pos_counter = 0
    deg_counter = len(number)
    number_in_dec = 0

    while pos_counter < len(number):
        deg_counter -= 1
        number_in_dec = (number[pos_counter] * system ** deg_counter) + number_in_dec
        pos_counter += 1

    return int(number_in_dec)

# Общая функция для перевода из десятичной СС
def from_dec(system, number):
    if is_number(number):
        number = int(number)
        ostatok = 1
        lst = []

        while number >= system:
            ostatok = int(number % system)
            number = number / system
            if system == 16:
                if ostatok == 10:
                    ostatok = 'a'
                elif ostatok == 11:
                    ostatok = 'b'
                elif ostatok == 12:
                    ostatok = 'c'
                elif ostatok == 13:
                    ostatok = 'd'
                elif ostatok == 14:
                    ostatok = 'e'
                elif ostatok == 15:
                    ostatok = 'f'
                else:
                    pass
            lst.append(ostatok)
        number = int(number)
        if system == 16:
            if number == 10:
                number = 'a'
            elif number == 11:
                number = 'b'
            elif number == 12:
                number = 'c'
            elif number == 13:
                number = 'd'
            elif number == 14:
                number = 'e'
            elif number == 15:
                number = 'f'
            else:
                pass
        lst.append(number)
        lst = str(lst[::-1]).strip('[').strip(']').replace("'", "")
        return str(lst.replace(', ', '')).upper()
    else:
        return

# Перевод из двоичной в десятичную СС
def bin2dec(number):
    number = list(number.strip(''))
    counter = 0

    while counter < len(number):
        if is_number(number[counter]):
            number[counter] = int(number[counter])
            if number[counter] >=0 and number[counter] <= 1:
                pass
            else:
                return
        else:
            return
        counter += 1

    return to_dec(2, number)

# Перевод из восьмеричной в десятичную СС
def oct2dec(number):
    number = list(number.strip(''))
    counter = 0

    while counter < len(number):
        if is_number(number[counter]):
            number[counter] = int(number[counter])
            if number[counter] >= 0 and number[counter] <= 7:
                pass
            else:
                return
        else:
            return
        counter += 1

    return to_dec(8, number)

# Перевод из шестнадцатиричной в десятичную СС
def hex2dec(number):
    number = list(number.strip(''))
    counter = 0

    while counter < len(number):
        if not is_number(number[counter]):
            if number[counter].lower() == 'a':
                number[counter] = 10
            elif number[counter].lower() == 'b':
                number[counter] = 11
            elif number[counter].lower() == 'c':
                number[counter] = 12
            elif number[counter].lower() == 'd':
                number[counter] = 13
            elif number[counter].lower() == 'e':
                number[counter] = 14
            elif number[counter].lower() == 'f':
                number[counter] = 15
            else:
                return
        else:
            number[counter] = int(number[counter])
        counter += 1

    return to_dec(16, number)

# Перевод из десятичной в двоичную СС
def dec2bin(number):
    return from_dec(2, number)

# Перевод из десятичной в восьмеричную CC
def dec2oct(number):
    return from_dec(8, number)

# Перевод из десятичной в шестнадцатиричную CC
def dec2hex(number):
    return from_dec(16, number)
