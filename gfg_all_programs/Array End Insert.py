# Given an array arr that is not completely filled and a value val, 
# you have to insert the value at the end of the array.

class Solution:
    def insertAtEnd(self, arr, val):
        # append() adds element at the end of the list
        arr.append(val)