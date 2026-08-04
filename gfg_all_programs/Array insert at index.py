# You are given an array arr(0-based index) and two positive integer index and val. 
# You need to insert an val at given index.

class Solution:
    def insertAtIndex(self, arr, index, val):
        # Insert val at the given index
        arr.insert(index, val)
        return arr
