#bubble sort
'''arr = list(map(int, input("enter elements:").split()))
n = len(arr)
for i in range(n):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print("sorted array:", arr)'''

#selection sort
'''arr = list(map(int, input("enter elements:").split()))
n = len(arr)
for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
print("sorted array:", arr)'''

#insertin sort
'''arr = list(map(int, input("enter elements:").split()))
for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
print("sorted array:", arr)'''

#merge sort
'''def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
arr = list(map(int, input("enter elements:").split()))
sorted_arr = merge_sort(arr)
print("sorted array:", sorted_arr)'''

#flipsort/pancake sort
'''def flip(arr, k):
    start = 0
    while start < k:
        arr[start], arr[k] = arr[k], arr[start]
        start += 1
        k -= 1
def pancake(arr):
    n = len(arr)
    for i in range(n-1, 0, -1):
        max_index = 0
        for j in range(1, i+1):
            if arr[j] > arr[max_index]:
                max_index = j
        if max_index != 0:
            flip(arr, max_index)
        flip(arr, i)
    return arr
arr = list(map(int, input("Enter elements:").split()))
sortedarray = pancake(arr)
print("Sorted array:", sortedarray)'''

#Quick sort
def quick(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick(arr, low, pi-1)
        quick(arr, pi+1, high)
def partition(arr, low, high):
    pivot = arr[high]
    i = low-1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1
arr = list(map(int, input("enter elements:").split()))
quick(arr, 0, len(arr)-1)
print("Sorted array:", arr)
