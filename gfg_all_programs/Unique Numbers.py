# In the given range [L, R], print all numbers having unique digits. 
# e.g. In range 10 to 20 should print all numbers except 11.

class Solution:
    def uniqueNumbers(self, L, R):
        arr_new = []
        
        # Iterate through the range [L, R]
        for num in range(L, R + 1):
            num_str = str(num)
            # A set only stores unique elements
            # If the lengths match, all digits were unique
            if len(set(num_str)) == len(num_str):
                arr_new.append(num)
                
        return arr_new