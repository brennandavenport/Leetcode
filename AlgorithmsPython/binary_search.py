#binary search
def binary_search(array, target):
    low = 0
    high = len(array)-1
    while low <= high:
        middle = int((low + high)/2)
        if array[middle] == target:
            return middle
        elif array[middle] > target:
            high = middle - 1 
        else:
            low = middle + 1
    return None

array = [2,4,5,6,7,8,19,20,23,24,30]

target = 2

print(binary_search(array, target))
