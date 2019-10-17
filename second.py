#opening a file with lists
import time
from datetime import datetime
file = open("ai183.txt", "r")
array = []
firstTest = False
secondTest = False

while True:
    check = file.read(1)
    if not check:
        break

    if check == "1":
        check = file.read(1)
        if check == "9":
            firstTest = True
            check = file.read(1)
            if check == ":":
                secondTest = True

    if firstTest == True and secondTest == True:
        file.seek(file.tell() + 1)
        check = file.read(1)
        while check != "}":
            array.append(int(check))
            check = file.read(1)
        break

file.close()
print("Array: ", array)

#quick sotring

def quickSort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        first = array[0]
        for number in array:
            if number < first:
                less.append(number)
            elif number == first:
                equal.append(number)
            elif number > first:
                greater.append(number)
        return quickSort(less) + equal + quickSort(greater)
    else:
        return array


start_time = datetime.now()
print("Quick sorted array: ", quickSort(array))
end_time = datetime.now()
print('---Duration: {}'.format(end_time - start_time))

#heap sorting

def heapSort(array):
    length = len(array)

    for i in range(length, -1, -1):
        heapExtra(array, length, i)

    for i in range(length - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapExtra(array, i, 0)
    return array

def heapExtra(array, length, i):
    largest = i
    L = 2 * i + 1
    R = 2 * i + 2

    if L < length and array[i] < array[L]:
        largest = L

    if R < length and array[largest] < array[R]:
        largest = R

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapExtra(array, length, largest)


start_time = datetime.now()
print("Heap sorted array: ", heapSort(array))
end_time = datetime.now()
print('---Duration: {}'.format(end_time - start_time))

#merge sorting
def mergeSort(array):
    if len(array) < 2: return array

    result, mid = [], int(len(array) / 2)

    right = mergeSort(array[mid:])
    left = mergeSort(array[:mid])

    while (len(left) > 0) and (len(right) > 0):
        if left[0] > right[0]:
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))

    result.extend(left + right)
    return result


start_time = datetime.now()
print("Merge sorted array: ", mergeSort(array))
end_time = datetime.now()
print('---Duration: {}'.format(end_time - start_time))
