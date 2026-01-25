# Given a sorted array, arr[] and a number target, 
# you need to find the number of occurrences of target in arr[]. 
class Solution:
    def countFreq(self, arr, target):
        count = 0                      # initialize count
        
        for num in arr:                # traverse array
            if num == target:          # if target found
                count += 1             # increase count
            elif num > target:         # if current number exceeds target
                break                  # stop loop (array is sorted)
        
        return count                   # return frequency