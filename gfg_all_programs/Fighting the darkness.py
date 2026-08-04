# Given an array arr[] representing the size of candles 
# which is reduced by 1 unit each day. 
# The room is illuminated using all the present candles. 
# Find the maximum number of days the room will stay illuminated 
# (at least one candle having a size greater than 0)

class Solution:
    def maxDays(self, arr):
        return max(arr)