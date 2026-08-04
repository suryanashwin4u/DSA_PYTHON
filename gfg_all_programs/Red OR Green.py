# Given a string of length N, made up of only uppercase characters 'R' and 'G', 
# where 'R' stands for Red and 'G' stands for Green.
# Find out the minimum number of characters you need to change to make the whole string of the same colour.

class Solution:
    def RedOrGreen(self, N, S):
        count_R = S.count('R')
        count_G = S.count('G')
        
        return min(count_R, count_G)