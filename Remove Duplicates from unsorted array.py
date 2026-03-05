# Given an array arr of integers which may or may not contain duplicate elements. 
# Your task is to remove duplicate elements.
class Solution:
    def removeDuplicate(self, arr):
        seen = set()
        result = []
        
        for num in arr:
            if num not in seen:
                seen.add(num)
                result.append(num)

        return result