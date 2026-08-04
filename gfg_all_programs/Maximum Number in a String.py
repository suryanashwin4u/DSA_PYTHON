# Given an alphanumeric string s consisting of lowercase letters (a–z), uppercase letters (A–Z), and digits (0–9).

# Extract all numeric substrings from s and return the maximum numeric value among them.

# If no numeric substring exists, return -1.

# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def extractMaximum(self, s):
        max_num = -1
        current = ""

        for ch in s:
            if ch.isdigit():
                current += ch
            else:
                if current:
                    max_num = max(max_num, int(current))
                    current = ""

        # Check last number if string ends with digit
        if current:
            max_num = max(max_num, int(current))

        return max_num