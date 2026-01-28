# Given a number n. 
# The task is to print Floyd's triangle with n lines.

class Solution:
    def printFloydTriangle(self, n):
        num = 1  # starting number

        for i in range(1, n + 1):      # rows
            for j in range(i):         # elements in each row
                print(num, end=" ")
                num += 1
            print()                    # new line after each row