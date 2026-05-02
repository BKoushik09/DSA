#square pattern
'''n = int(input("enter the value of n:"))
for i in range(n):
    for j in range(n):
        print("*", end = " ")
    print()'''

#hollow square pattern
'''n = int(input("enter the value of n:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()'''

#hollow diagonal square pattern
'''n = int(input("enter the value of n:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==j:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()'''

#anti-hollow diagonal square pattern
'''n = int(input("enter the value of n:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==j or (i+j)==n-1:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()'''

#hour glass shape
'''n = int(input("enter the value of n:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i+j==n-1 or i==j:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()'''

#plus/cordinate shape
'''n = int(input("enter the value of n:"))
for i in range(n):
    for j in range(n):
        if i==n//2 or j==n//2:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()'''

#asterik shape
'''n = int(input("enter the value of n:"))
for i in range(n):
    for j in range(n):
        if i==n//2 or j==n//2 or i==j or (i+j)==n-1:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()'''


#right angle triangle pattern
'''n = int(input("enter the value of n:"))
for i in range(n):
    for j in range(i+1):
        print("*", end = " ")
    print()'''

#mirror right angle triangle pattern
'''n = int(input("enter the value of n:"))
for i in range(n):
    for j in range(n):
        if j>=n-i-1:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()'''

#hollow right angle triangle pattern
'''n = int(input("enter the value of n:"))
for i in range(n):
    for j in range(i+1):
        if j==0 or j==i or i==n-1:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()'''

#mirror hollow right angle triangle pattern
'''n = int(input("enter the value of n:"))
for i in range(n):
    for j in range(n):
        if j==n-i-1 or j==n-1 or i==n-1:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()'''

'''n = int(input("enter the value of n:"))
for i in range(n):
    for j in range(i):
        print(j, end = ' ')
    print()'''

#pyramid pattern
'''n = int(input("enter the value of n:"))
for i in range(n):
    for j in range(n-i-1):
        print(" ", end = " ")
    for k in range(2*i+1):
        print("*", end = " ")
    print()'''

n = 5
for i in range(n):
    for j in range(i+1, n-1):
        print(j)
    print()