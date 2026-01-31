# Given an array arr[] of positive integers. 
# Return true if all the array elements are palindrome otherwise, return false.

def isPalinArray(arr):
    # Traverse each element in the array
    for num in arr:
        # Convert number to string and reverse it
        if str(num) != str(num)[::-1]:
            return False   # If any number is not palindrome
    return True            # All numbers are palindrome
