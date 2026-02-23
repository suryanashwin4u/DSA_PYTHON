# You are given an array arr. 
# Find the sum of distinct elements in an array.

class Solution:
    def findSum(self, arr):
        return sum(set(arr))