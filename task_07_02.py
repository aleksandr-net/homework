#!/usr/bin/python3.5
import random
import string


def password_generator(max):
    characters = string.punctuation + string.ascii_letters + string.digits

    while True:
        yield ''.join([random.choice(characters) for i in range(max)])

if __name__ == '__main__':
    print(password_generator(8))
    print(next(password_generator(8)))

