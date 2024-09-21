def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while array[j - 1] > array[j] and j > 0:
            array[j - 1], array[j] = array[j], array[j -1] #swaps
            j -= 1
    return array



array = [2,5,8,4,3,1]
insertion_sort(array)
print(array)

