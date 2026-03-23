# Given a set of numbers from 1 to n, 
# each number is exactly present twice so there are n pairs. 
# In the worst-case scenario, 
# how many numbers X should be picked and 
# removed from the set until we find a matching pair

class Solution:
    def find(self, n):
        return n + 1