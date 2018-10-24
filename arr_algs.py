from functools import reduce


def raise_exception_for_incorrect_list(array):
    if not type(array) is list:
        raise TypeError("argument have not type list")
    elif not array:
        raise ValueError("list is empty")


def find_min(array):
    raise_exception_for_incorrect_list(array)
    return reduce(lambda accumulator, item: item if item < accumulator else accumulator, array)


def avr(array):
    raise_exception_for_incorrect_list(array)
    return reduce(lambda accumulator, item: accumulator + item, array) / (float)(len(array))


a = [2, 8, 9, 11, 78, 1]
try:
    print(find_min(a))
    print(avr(a))
except ValueError as e:
    print(e)
except TypeError as e:
    print(e)
b = []
try:
    print(find_min(b))
    print(avr(b))
except ValueError as e:
    print(e)
except TypeError as e:
    print(e)
