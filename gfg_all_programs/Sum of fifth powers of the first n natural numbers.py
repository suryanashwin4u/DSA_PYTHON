# Given a number N.Find the sum of fifth powers of natural numbers till N i.e. 15+25+35+..+N5.

class Solution:
    def sumOfFifthPowers(self, N):
        return (N*N * (N+1)*(N+1) * (2*N*N + 2*N - 1)) // 12

