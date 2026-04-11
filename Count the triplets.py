# Given an array arr, count the number of distinct triplets (a, b, c) such that:

# a + b = c

# Each triplet is counted only once, regardless of the order of a and b.

class Solution:
    def countTriplet(self, arr):
        n = len(arr)
        arr.sort()
        count = 0
        
        # Iterate from the end of the array to the beginning
        # i is the index of our target sum 'c'
        for i in range(n - 1, 1, -1):
            target = arr[i]
            left = 0
            right = i - 1
            
            while left < right:
                current_sum = arr[left] + arr[right]
                
                if current_sum == target:
                    count += 1
                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return count