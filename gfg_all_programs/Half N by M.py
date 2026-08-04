# Given two values N and M. Give the value when N is halved M-1 times.

class Solution:
    def mthHalf(self, N, M):
        return N // (2 ** (M - 1))

#OR
class Solution:
    def mthHalf(self, N, M):
        return N >> (M - 1)