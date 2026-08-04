# You are given a string s. 
# You need to find the length of the string and return it.

class Solution:
    def lengthString(self, str):
        count = 0

        for ch in str:
            count += 1
        return count
    