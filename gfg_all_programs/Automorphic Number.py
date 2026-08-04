# Given a number n, check whether the number is an Automorphic number or not. 
# A number is called an Automorphic number if and only if the square of the number ends with the number itself.

class Solution:
    def isAutomorphic(self, n):
        sq = n * n
        return "Automorphic" if str(sq).endswith(str(n)) else "Not Automorphic"

