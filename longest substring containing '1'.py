# Given a function that takes a binary string. 
# The task is to return the longest size of contiguous substring containing only ‘1’.

def maxlength(s):
    max_len = 0
    count = 0

    for ch in s:
        if ch == '1':
            count += 1
            max_len = max(max_len, count)
        else:
            count = 0

    return max_len