# Given a number N. 
# Check if it is perfect or not. 
# A number is perfect if sum of factorial of its digit is equal to the given number.

#User function Template for python3
class Solution:
    def isPerfect(self, N):
        temp = N
        total = 0

        while N > 0:
            digit = N % 10

            fact = 1
            for i in range(1, digit + 1):
                fact *= i

            total += fact
            N //= 10

        if total == temp:
            return 1
        else:
            return 0