#LINEAR SEARCH
'''arr = list(map(int, input("enter elements:").split()))
target = int(input("enter the element to be searched:"))
found = False
for i in range(len(arr)):
    if arr[i] == target:
        print("element found at index:", i)
        found = True
        break
if not found:
    print("element not found")'''

'''for i in arr:
    if i == target:
        print("element found at index:", arr.index(i))
        found = True
        break
if not found:
    print("element not found")'''

#BINARY SEARCH
'''arr = list(map(int, input("enter elements:").split()))
arr.sort()
target = int(input("enter the element to be searched:"))
found = False
left = 0
right = len(arr)-1
while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        print("element found at index:", mid)
        found = True
        break
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
if not found:
    print("element not found")'''

#JUMP SEARCH
import math
arr = list(map(int, input("enter elements:").split()))
target = int(input("enter the element to be searched:"))
n = len(arr)
step = int(math.sqrt(n))
i = 0
while i < n and arr[min(i+step, n)-1] < target:
    i += step
for j in range(i, min(i+step, n)):
    if arr[j] == target:
        print("element found at index:", j)
        break
else:
    print("element not found")