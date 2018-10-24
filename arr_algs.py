from functools import reduce


def find_min(array):
    return reduce(lambda accumulator, item: item if item < accumulator else accumulator, array)


def avr(array):
    return reduce(lambda accumulator, item: accumulator + item, array) / (float)(len(array))


a = [2, 8, 9, 11, 78, 1]
print(find_min(a))
print(avr(a))
b = []
print(find_min(b))
print(avr(b))
