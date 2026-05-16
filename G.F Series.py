# Geek made a special series and named it as G.F Series. 
# The series follows this trend  Tn = (Tn-2)2 - (Tn-1)  in which the first and the second term are 0 and 1 respectively. 
# Help Siddhant to find the first n terms of the series.

# Note: Print a white space (" ") after every integer and a newline character after every testcase.

# Time Complexity: O(n)
# Auxiliary Space: O(n)

class Solution:
    def gfSeries(self, n):
        arr = [0, 1]

        for i in range(2, n):
            arr.append(arr[i-2]**2 - arr[i-1])

        print(*arr[:n]) # * used to unpack list 