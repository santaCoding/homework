#selection sort

list = [310, 464, 375, 922, 592, 800, 426, 430, 279, 137, 170, 440, 555, 658, 520]
print('\n---Unsorted list: ', list, '\n')

def selectionSort(list):
    for index in range(len(list)):
        for min in range(index+1, len(list)):
            if list[min] < list[index]:
                list[min], list[index] = list[index], list[min]
    return list
        
list = selectionSort(list)
print('---Sorted list (selection sort): ', list, '\n')

#insertion sort

list2 = [407, 192, 901, 308, 271, 24, 436, 433, 822, 527, 805, 385, 144, 792, 287]
print('\n---Unsorted list: ', list2, '\n')

def insertionSort(list2):
    for index in range(len(list2)):
        j = index - 1
        key = list2[index]
        while list2[j] > key and j >= 0:
            list2[j + 1] = list2[j]
            j -= 1
        list2[j + 1] = key
    return list2

list2 = insertionSort(list2)
print('---Sorted list (insertion sort): ', list2, '\n')
