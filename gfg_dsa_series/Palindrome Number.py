# You are given an integer n. Your task is to find if it is a palindrome.

# Time Complexity: O(d), d is number of digits in n
# Auxiliary Space: O(1)

class Solution:
    def isPalindrome(self, n: int) -> bool:
        # Ignore sign as specified in problem constraints
        n = abs(n)
        
        temp = n
        reversed_num = 0
        
        while temp > 0:
            reversed_num = (reversed_num * 10) + (temp % 10)
            temp //= 10
            
        return reversed_num == n
    
# or

class Solution:
    def isPalindrome(self, n: int) -> bool:
        s = str(abs(n))
        return s == s[::-1]