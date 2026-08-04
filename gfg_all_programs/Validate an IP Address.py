# You are given a string s in the form of an IPv4 Address. Your task is to validate an IPv4 Address, if it is valid return true otherwise return false.

# IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255, separated by dots, e.g., "172.16.254.1"

# A valid IPv4 Address is of the form x1.x2.x3.x4 where 0 <= (x1, x2, x3, x4) <= 255. Thus, we can write the generalized form of an IPv4 address as (0-255).(0-255).(0-255).(0-255)

# Note: Here we are considering numbers only from 0 to 255 and any additional leading zeroes will be considered invalid.

# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def isValid(self, s):
        
        parts = s.split('.')
        
        # Must contain exactly 4 parts
        if len(parts) != 4:
            return False
        
        for part in parts:
            
            # Empty part not allowed
            if part == "":
                return False
            
            # Only digits allowed
            if not part.isdigit():
                return False
            
            # Leading zeros not allowed
            if len(part) > 1 and part[0] == '0':
                return False
            
            # Range check
            if int(part) < 0 or int(part) > 255:
                return False
        
        return True