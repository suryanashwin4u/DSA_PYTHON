# Numbers have a measure of friendliness defined as the absolute difference between them. 
# Given an circular array of integers arr[], calculate the friendliness of the array. 
# Friendliness is the sum of the absolute differences between each element and its closest friend in the array.

class Solution:
    def calculateFriendliness(self, arr):
        n = len(arr)
        total = 0
        
        for i in range(n):
            total += abs(arr[i] - arr[(i + 1) % n])
        
        return total

