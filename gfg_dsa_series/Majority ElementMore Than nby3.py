# Given an array arr[] consisting of n integers, 
# find all the array elements which occurs more than floor(n/3) times.
#  Return the resulting array in strictly increasing order. 
# If no such elements exist, return an empty array.

# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def findMajority(self, arr):
        n = len(arr)
        if n == 0:
            return []

        # 1. Candidate Selection
        ele1, ele2 = None, None
        cnt1, cnt2 = 0, 0

        for num in arr:
            if ele1 == num:
                cnt1 += 1
            elif ele2 == num:
                cnt2 += 1
            elif cnt1 == 0:
                ele1 = num
                cnt1 = 1
            elif cnt2 == 0:
                ele2 = num
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        # 2. Verification Pass
        cnt1, cnt2 = 0, 0
        for num in arr:
            if num == ele1:
                cnt1 += 1
            elif num == ele2:
                cnt2 += 1

        # 3. Collect valid candidates
        res = []
        if cnt1 > n // 3:
            res.append(ele1)
        if cnt2 > n // 3:
            res.append(ele2)

        return sorted(res)