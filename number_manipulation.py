'''a = 30
b = 20
print(" a address:", id(a))
print(" b address:", id(b))
c = a + b
print(c)
print(" c address:", id(c))'''

'''num = int(input("enter a number:"))
copy = num
sum = 0
while num!=0:
    rem = num%10
    sum += rem**3
    num//=10
if copy == sum:
    print(num, "is an armstrong number")
else:
    print(num, "is not an armstrong number")'''

#Niven's number
'''n = int(input("enter a number:"))
copy = n
sum = 0
while n!=0:
    rem = n%10
    sum += rem
    n//=10
if copy%sum == 0:
    print(copy, "is a niven's number")
else:
    print(copy, "is not a niven's number")'''

#Factorial of a number
'''n = int(input("enter a number:"))
fact = 1
i = 1
while i<=n:
    fact *= i
    i+=1
print("factorial of", n, "is:", fact)'''

#Strong number
num = int(input("enter a number:"))
temp = num
sum = 0
while temp>0:
    r = temp%10
    fact = 1
    i = 1
    while i<=r:
        fact *= i
        i+=1
    sum += fact
    temp//=10
if sum == num:
    print(num, "is a strong number")
else:
    print(num, "is not a strong number")