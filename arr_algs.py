from functools import reduce


def is_empty(func):
    def wrapper(array):
        if not array:
            raise ValueError("list is empty")
        else:
            return func(array)
    return wrapper


def is_list(func):
    def wrapper(array):
        if not type(array) is list:
            raise TypeError("argument have not type list")
        else:
            return func(array)
    return wrapper


@is_empty
@is_list
def find_min(array):
    return reduce(lambda accumulator, item: item if item < accumulator else accumulator, array)


@is_empty
@is_list
def avr(array):
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
