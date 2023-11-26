#!/usr/bin/env python3

def print_fibonacci(length):
    pass
    fib_sequence = []
    a, b = 0, 1
    for _ in range(length):
        fib_sequence.append(a)
        a, b = b, a + b

    if length == 0:
        print('[]')
    else:
        print(fib_sequence)
print_fibonacci(0)