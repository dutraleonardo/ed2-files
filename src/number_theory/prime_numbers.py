#!/usr/bin/env python3
"""
    module to operations with prime numbers
"""


def check_prime(number):
        """
            it's not the best solution
        """
        return all([number % i for i in range(2, number)])


def next_prime(value, factor=1, **kwargs):
    value = factor * value

    if value is 0 or 1:
        return 2

    while not check_prime(value):
            value += -1 if ("desc" in kwargs.keys() and kwargs["desc"] is True) else 1

    return value
