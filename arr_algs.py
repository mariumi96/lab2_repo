from functools import reduce


def avr(arr):
    if arr:
        a = 0
        for el in arr:
            a = a + el
        n = len(arr)
        return a / n
    else:
        print('Массив пуст!')
def find_min(array):
    return reduce(lambda accumulator, item: item if item < accumulator else accumulator, array)




a = [2, 8, 9, 11, 78, 1]
print(find_min(a))
print(avr(a))
b = []
print(find_min(b))
print(avr(b))
