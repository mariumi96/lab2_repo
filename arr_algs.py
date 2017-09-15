def find_min(arr):
    if(arr):
        min=arr[0]
        for el in arr:
            if el<min:
                min=el
        return min
    else:
        print('Массив пуст!')
def avr(arr):
    if (arr):
        a = 0
        for el in arr:
            a=a+el
        n=len(arr)
        return a/n
    else:
        print('Массив пуст!')
a=[2,8,9,11,78,1]
print(find_min(a))
print(avr(a))
b=[]
print(find_min(b))
print(avr(b))