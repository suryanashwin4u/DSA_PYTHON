# Given a string s containing only lowercase alphabets, the task is to sort it in lexicographically-descending order.
# Note : A string is in lexicographically descending order if characters are arranged from larger to smaller based on dictionary order (i.e., 'z' comes before 'a').

# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def reverseSort(self, s):
        return "".join(sorted(s, reverse=True))

#or

class Solution:
    def reverseSort(self, s):
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - 97] += 1

        return ''.join(chr(i + 97) * freq[i] for i in range(25, -1, -1))