# Given an array arr, use selection sort to sort arr[] in increasing order.

class Solution:
    def selectionSort(self, arr):
        n = len(arr)
        
        for i in range(n - 1):
            min_idx = i
            
            # Find minimum in remaining array
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            
            # Swap
            arr[i], arr[min_idx] = arr[min_idx], arr[i]