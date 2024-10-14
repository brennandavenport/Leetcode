'''
import time

#Creates a stack overflow error
#Too many recursive calls

def recursion(num):
    print("Number of calls: ", num)
    time.sleep(0.01)
    if num > 0:
        recursion(num + 1)
    

recursion(1)


def sum(array):
    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[0]
    num = array[0]
    array.pop(0)
    return num + sum(array)

arr= [1,2,3,9,10]

print(sum(arr))


def counting(list):
    count = 1
    if len(list) == 0:
        return 0
    list.pop()
    return count + counting(list)



arr= ["apple", "car", "orange"]
print(counting(arr))



def max_num(array):
    if len(array) == 1:
        return array[0]
    elif len(array) == 0:
        return None
    elif array[0] > array[1]:
        array.pop(1)
    else:
        array.pop(0)
    print(array)
    return max_num(array)
    

array = [10,5,5,20]
print(max_num(array))



def binary_search(array, target, low, high):
    if len(array) == 1:
        return array[0]
    elif len(array) == 0:
        return None
    
    if (low > high):
        return -1
    
    middle = (low + high) // 2
    if (array[middle] == target):
        return middle
    elif (array[middle] > target):
        return binary_search(array, target, low, middle - 1)
    else:
        return binary_search(array, target, middle + 1, high)
    

arr = [1,3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57,60]

print(binary_search(arr, 61, 0, len(arr)-1))

'''

book = dict()
book["Apple"] = 1.00
book["Banana"] = 1.50
book["Lettuce"] = 3.00

print(book["Lettuce"])

phone_nums = {}

phone_nums["Mom"] = 1234567890
phone_nums["Dad"] = 9091234567
phone_nums["Emergency"] = 911

print(phone_nums.get("Momm"))


array = ["Orange", "Potato"]
for i in range(len(array)):
    phone_nums[array[i]] = i

print(phone_nums)    