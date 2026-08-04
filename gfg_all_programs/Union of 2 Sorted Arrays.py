# Given two sorted arrays a[] and b[], where each array may contain duplicate elements , the task is to return the elements in the union of the two arrays in sorted order.
# Union of two arrays can be defined as the set containing distinct common elements that are present in either of the arrays.

class Solution:
    def findUnion(self, a, b):
        i, j = 0, 0
        n, m = len(a), len(b)
        result = []
        
        while i < n and j < m:
            # Skip duplicates in a
            if i > 0 and a[i] == a[i - 1]:
                i += 1
                continue
            
            # Skip duplicates in b
            if j > 0 and b[j] == b[j - 1]:
                j += 1
                continue
            
            if a[i] < b[j]:
                result.append(a[i])
                i += 1
            elif a[i] > b[j]:
                result.append(b[j])
                j += 1
            else:
                result.append(a[i])
                i += 1
                j += 1
        
        # Remaining elements of a
        while i < n:
            if i == 0 or a[i] != a[i - 1]:
                result.append(a[i])
            i += 1
        
        # Remaining elements of b
        while j < m:
            if j == 0 or b[j] != b[j - 1]:
                result.append(b[j])
            j += 1
        
        return result