""" Functions for doing calculations. """
import math
import cmath


def add(lh, rh):
    return lh + rh


def subtract(lh, rh):
    return lh - rh


def divide(left_hand, right_hand):
    return lh/rh


class MyError(Exception):
    pass


def raise_error():
    raise MyError("Ouch, something went wrong!")


def sqrt(value):
    return math.sqrt(value)


def csqrt(value):
    return cmath.sqrt(value)


if __name__ == "__main__":
    print(f"1+2 = {add(1, 2)}")
    print(f"2-1 = {subtract(2, 1)}")
