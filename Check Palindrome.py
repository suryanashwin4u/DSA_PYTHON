# Given a string s, you need to check if it is palindrome or not. 
# A palidrome is a string that reads the same from front and back.
# Note: Ignore the case in this question.

def isPalindrome(s):
    s = s.lower()        # Step 1: ignore case
    return s == s[::-1]  # Step 2: compare with reverse
