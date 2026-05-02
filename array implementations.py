#rotate an array to the right by 1
'''arr = list(map(int, input("enter values:").split()))
last  = arr[-1]
for i in range(len(arr)-1, 0, -1):
    arr[i] = arr[i-1]
arr[0] = last
print("rotated array:", arr)'''

#move all zeroes to the end of the array
'''arr = list(map(int, input("enter values:").split()))
zero = 0
for i in range(len(arr)):
    if arr[i] != 0:      # if arr[i] == 0 ()--> to print zeroes at the start of the array
        arr[zero], arr[i] = arr[i], arr[zero]
        zero += 1
print("array after moving zeroes to the end:", arr)'''

#reverse an array
'''arr = list(map(int, input("enter values:").split()))
start = 0
end = len(arr)-1
while start<end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1
print("reversed array:", arr)'''

#sub array with maximum sum (Kadane's algorithm)
'''arr = list(map(int, input("enter values:").split()))
max_sum = arr[0]
current = arr[0]
for i in range(1, len(arr)):
    current = max(arr[i], current+arr[i])
    max_sum = max(max_sum, current)
print("maximum subarray sum is:", max_sum)'''