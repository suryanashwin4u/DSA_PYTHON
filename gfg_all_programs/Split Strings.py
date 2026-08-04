# Given a string S which consists of alphabets , 
# numbers and special characters. 
# You need to write a program to split the strings in three different strings
# S1, S2 and S3 such that the string S1 will contain all the alphabets present in S , 
# the string S2 will contain all the numbers present in S and S3 will contain all special characters present in S.  
# The strings S1, S2 and S3 should have characters in same order as they appear in input.

class Solution:
    def splitString(self, S):
        s1 = ""
        s2 = ""
        s3 = ""
        
        for ch in S:
            if ch.isalpha():
                s1 += ch
            elif ch.isdigit():
                s2 += ch
            else:
                s3 += ch
        
        return [s1, s2, s3]