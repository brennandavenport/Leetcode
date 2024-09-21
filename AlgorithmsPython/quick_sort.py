def quick_sort(array):
    if len(array) < 2:
        return array
    else: 
        pivot = array[0]

        less = [i for i in array[1:] if i <= pivot]

        greater = [i for i in array[1:] if i > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)

arr = [3,4,3,2,3,5,3,4,3,2,4,3,4,1,2,4,3,2,5,2,3,6,7,9,6,7,8,9,6,9,8,6,9,8,7,1]
#print(quick_sort(arr))

array = [9,4,6,7,5,8,10,2,5]

# for item in array:
#     print(item)

pivot = array[0]

list = []
for i in array[1:]:
    if i <= pivot:
        list.append(i)

print(list)