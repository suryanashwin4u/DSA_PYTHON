# Given an array arr[]. 
# The task is to find the number of odd and even elements in the array.
# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(1)

class Solution:
    def countOddEven(self, arr):
        odd = 0
        even = 0
        
        for num in arr:
            if num % 2 == 0:
                even += 1
            else:
                odd += 1
                
        print(odd, even)