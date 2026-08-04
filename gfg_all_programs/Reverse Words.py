# Given a string s, 
# reverse the string without reversing its individual words. 
# Words are separated by dots(.).
# Note: The string may contain leading 
# or 
# trailing dots(.) 
# or 
# multiple dots(.) between two words. 
# The returned string should only have a single dot(.) separating the words, 
# and no extra dots should be included.

class Solution:
    def reverseWords(self, s):
        # Step 1: Split string by dot
        words = s.split('.')
        
        # Step 2: Remove empty strings caused by extra dots
        clean_words = []
        for word in words:
            if word != "":
                clean_words.append(word)
        
        # Step 3: Reverse the list of words
        clean_words.reverse()
        
        # Step 4: Join words with a single dot
        return ".".join(clean_words)
