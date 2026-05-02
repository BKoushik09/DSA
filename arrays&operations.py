#accessing elements in an array
'''arr = list(map(int, input("enter the list of elements:").split()))
print(arr[2])
print(arr[-2])'''

#Traversal of array
'''arr = list(map(int, input("enter the list of elements:").split()))
for i in range(len(arr)):
    print(arr[i]+1, end = ' ')'''

#finding the minimum value in an array
'''arr =  list(map(int, input("enter the list of elements:").split()))
min_value = arr[0]
for i in arr:
    if i<min_value:
        min_value = i
print("the minimum value in the array is:", min_value)'''

#finding the maximum value in an array
'''arr =  list(map(int, input("enter the list of elements:").split()))
max_value = arr[0]
for i in arr:
    if i>max_value:
        max_value = i
print("the maximum value in the array is:", max_value)'''

#to reverse the words in given string
'''words = input("enter the list of words:").split()
for word in words:
    print(word[::-1], end = " ")'''

#finding the smallest word in a list of words (the word with the least number of characters)
'''words = input("enter the list of words:").split()
smallest_word = words[0]
for word in words:
    if len(word)<len(smallest_word):
        smallest_word = word
print("the smallest word in the list is:", smallest_word)'''

#to find smallest word lexicographically in a list of words
'''words = input("enter the list of words:").split()
smallest_word = words[0]
for word in words:
    if word<smallest_word:
        smallest_word = word
print("the smallest word in the list is:", smallest_word)'''

#encrypt a word using caesar cipher
'''word = input("enter the word:")
key = int(input("enter the key:"))
result = ""
for ch in word:
    if ch.isalpha():
        if ch.islower():
            new = chr(ord(ch)+key)
            result += new
        else:
            new = chr(ord(ch)+key)
            result += new
print(result)'''


#array insertion
'''a = list(map(int, input("enter the elements:").split()))
print("before using insert method:", a)
index = int(input())
value = int(input())
a.insert(index, value)
print(a)'''

'''a = list(map(str, input("enter the elements:").split()))
print("before using insert method:", a)
index = int(input())
value = input()
a.insert(index, value)
print(a)'''

#array insertion and deletion
'''n = int(input("enter the number of elements:"))
a = []
for i in range(n):
    a.append(int(input("enter elements:")))
print("Array before deletion:", a)
value = int(input("enter the value to delete:"))
a.remove(value)
print("array after deletion:", a)'''

#array searching
'''arr = list(map(int, input("enter elements with spaces:").split()))
search = int(input("enter element to be searched:"))
found = False
for i in range(len(arr)):
    if arr[i] == search:
        print("Element found at index:", i)
        found = True
        break
if not found:
    print("element not found")'''

'''string = input("enter any string:").strip()  #for single string
#string = input("enter elements with spaces:").split() #for multiple strings
search = input("enter any char/string to be searched:")
found = False
for i in range(len(string)):
    if string[i] == search:
        print("Element found at index:", i)
        found = True
        break
if not found:
    print("element not found")'''

#finding the list of elements greater than 3
'''arr = list(map(int, input("enter the list of numbers:").split()))
num = 3
lst = []
found = False
for i in arr:
    if i > num:
        lst.append(i)
        found = True
print(lst)
if not found:
    print("no element found")'''

#missing element in an array
'''arr = list(map(int, input("enter the list of numbers:").split()))
n = len(arr)+1
e_sum = n*(n+1)//2
o_sum = sum(arr)
print("missing number:", e_sum - o_sum)'''