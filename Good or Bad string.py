# In this problem, a String S is composed of lowercase alphabets and wildcard characters i.e. '?'. Here, '?' can be replaced by any of the lowercase alphabets. Now you have to classify the given String on the basis of following rules:
# If there are more than 3 consonants together or more than 5 vowels together, the String is considered to be "BAD". A String is considered "GOOD" only if it is not “BAD”.
# NOTE: String is considered as "BAD" if the above condition is satisfied even once. Else it is "GOOD" and the task is to make the string "BAD".

class Solution:
    def isGoodorBad(self, S):
        vowels = set('aeiou')

        v = 0   # consecutive vowels
        c = 0   # consecutive consonants
        
        for ch in S:            
            if ch in vowels:
                v += 1
                c = 0
                
            elif ch == '?':
                v += 1
                c += 1
                
            else:
                c += 1
                v = 0
            
            if v > 5 or c > 3:
                return 0
            
        return 1