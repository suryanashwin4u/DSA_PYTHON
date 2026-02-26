# Given a number N. Check whether it is divisble by 4.

class Solution:
    def divisibleBy4(self, N):
        # If length is 1, check directly
        if len(N) == 1:
            return 1 if int(N) % 4 == 0 else 0
        
        # Take last two digits
        last_two = int(N[-2:])
        
        return 1 if last_two % 4 == 0 else 0