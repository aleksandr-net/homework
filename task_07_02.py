#!/usr/bin/python3.5
import random
import string


def password_generator(max):
    characters = string.punctuation + string.ascii_letters + string.digits
    passwd = ''

    while max:
        passwd += random.choice(characters)
        max -= 1

    yield passwd