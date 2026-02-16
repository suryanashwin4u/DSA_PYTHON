# *********
#  *******
#   *****
#    ***
#     *

class Solution:
    def printTriangle(self, N):
        for i in range(N):
            # print spaces
            print(" " * i, end="")
            
            # print stars
            print("*" * (2*(N-i)-1))
