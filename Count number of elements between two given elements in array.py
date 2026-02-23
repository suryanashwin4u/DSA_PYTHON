# Given an unsorted array arr[] and two elements num1 and num2. 
# The task is to count the number of elements that occur between the given elements (excluding num1 and num2). 
# If there are multiple occurrences of num1 and num2, we need to consider the leftmost occurrence of num1 and the rightmost occurrence of num2.

class Solution:
    def getCount(self, arr, num1, num2):
        first = -1
        last = -1
        
        # Find leftmost num1
        for i in range(len(arr)):
            if arr[i] == num1:
                first = i
                break
        
        # Find rightmost num2
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] == num2:
                last = i
                break
        
        # If not found or invalid order
        if first == -1 or last == -1 or first >= last:
            return 0
        
        return last - first - 1