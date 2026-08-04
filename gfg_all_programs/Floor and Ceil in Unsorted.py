# Given an unsorted array arr[] of integers and an integer x, find the floor and ceiling of x in arr[].

# Floor of x is the largest element which is smaller than or equal to x. 
# Floor of x doesn’t exist if x is smaller than smallest element of arr[].
# Ceil of x is the smallest element which is greater than or equal to x. 
# Ceil of x doesn’t exist if x is greater than greatest element of arr[].
# Return an array of integers denoting the [floor, ceil]. 
# Return -1 for floor or ceiling if the floor or ceiling is not present.

# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        floor = -1
        ceil = -1

        for num in arr:
            if num <= x:
                if floor == -1 or num > floor:
                    floor = num

            if num >= x:
                if ceil == -1 or num < ceil:
                    ceil = num

        return [floor, ceil]