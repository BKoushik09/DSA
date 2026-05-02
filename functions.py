#no args and no return value (type-1)
'''def hi():
    print("hi")
    print("Good morning", end = " ")
    print("have a nice day")
hi()'''

#args and no return value (type-2)
'''def summate(a, b):
    sum = a + b
    print("the sum is", sum)
def diff(a, b):
    difference = a - b
    print("the difference is", difference)
a = int(input("enter a number:"))
b = int(input("enter another number:"))
summate(a, b)
diff(a, b)'''

#no args and return value (type-3)
'''def addition():
    a = int(input("enter a number:"))
    b = int(input("enter another number:"))
    c = a + b
    return c
summate = addition()
print("the sum is", summate)'''

#args and return value (type-4)
def expo(a,b):
    return a**b
x = int(input("enter a number:"))
y = int(input("enter another number:"))
result = expo(x,y)
print("the result is:", result)