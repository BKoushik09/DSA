#Recursions: a problem-solving technique where a function calls itself to solve a smaller instance of the same problem.
#important components of recursion: base case, recursive case
#types of recursions:
'''
1. Tail recursion: the recursive call is the last operation performed in the function.
2. Head recursion: the recursive call is the first operation performed in the function.
3. Tree recursion: a function makes multiple recursive calls, leading to a branching structure.
4. Indirect recursion: two or more functions call each other in a circular manner.
5. Nested recursion: a function calls itself within its own recursive call.
6.Direct recursion: a function calls itself directly.
'''

#Direct recursion
'''def nums(n):
    if n==0:
        return
    print(n, end = " ")
    nums(n-1)
n = int(input("enter a number:"))
nums(n)'''

#Indirect recursion
'''def funA(n):
    if n <= 0:
        return
    print('A', n)
    funB(n-1)
def funB(n):
    if n <= 0:
        return
    print('B', n)
    funA(n-1)
n = int(input("enter a number:"))
funA(n)'''

#example-2
'''def is_even(n):
    if n == 0:
        return True
    return is_odd(n-1)
def is_odd(n):
    if n == 0:
        return False
    return is_even(n-1)
n = int(input("enter a number:"))
if is_even(n):
    print(n, "is even")
else:
    print(n, "is not even")'''

#Nested recursion
'''def fun(n):                                  
    if n>10:
        return n-1
    return fun(fun(n+2))
N = int(input("enter a number:"))
print(fun(N))'''

#dry run for n=5
'''def fun(n):                                 
func(5) -> fun(fun(7)) -> fun(fun(fun(9))) -> fun(fun(fun(fun(11)))) -> fun(fun(fun(fun(10)))) -> 
fun(fun(fun(9))) -> fun(fun(8)) -> fun(7) -> fun(6) -> fun(5) -> fun(4) -> fun(3) -> fun(2) -> 
fun(1) -> fun(0) -> return'''