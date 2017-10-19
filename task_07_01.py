#!/usr/bin/python3.5
def fibonacci(max):
    fib1, fib2 = 0, 1
    while max:
        fib1, fib2 = fib2, fib1 + fib2
        max -= 1
        yield fib1