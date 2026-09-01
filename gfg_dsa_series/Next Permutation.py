# Given an array of integers arr[] representing a permutation, 
# implement the next permutation that rearranges the numbers into the lexicographically next greater permutation. 
# If no such permutation exists, rearrange the numbers into the lowest possible order (i.e., sorted in ascending order). 

# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def nextPermutation(self, arr):
        n = len(arr)
        
        # Step 1: Find the pivot element from right
        pivot = -1
        for i in range(n - 2, -1, -1):
            if arr[i] < arr[i + 1]:
                pivot = i
                break
        
        # If no pivot is found, the array is in descending order
        if pivot == -1:
            arr.reverse()
            return arr
        
        # Step 2: Find the element just greater than arr[pivot] from right
        for j in range(n - 1, pivot, -1):
            if arr[j] > arr[pivot]:
                arr[pivot], arr[j] = arr[j], arr[pivot]
                break
        
        # Step 3: Reverse elements after pivot
        arr[pivot + 1:] = reversed(arr[pivot + 1:])
        return arr