# Given an integer n. Write a program to find the nth Fibonacci number.
# F(0)= 0, F(1)=1
# The nth Fibonacci number is given by the forumla F(n) = F(n-1) + F(n-2). The first few fibonacci numbers are: 0 1 1 2 3 5. . . . 

n = int(input())

if n == 0:
    fib = 0
elif n == 1:
    fib = 1
else:
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    fib = b

print(fib)