# Given a string S, 
# remove all consonants and print the modified string that contains vowels only.

class Solution:
    def removeConsonants(self, s):
        vowels = "aeiouAEIOU"
        result = ""
        
        for ch in s:
            if ch in vowels:
                result += ch
        
        if result == "":
            return "No Vowel"
        
        return result