# You are given an array arr[], and you have to re-construct an array arr[].
# The values in arr[] are obtained by doing Xor of consecutive elements in the array.

def game_with_number(arr, n):
    # Traverse till second last element
    for i in range(n - 1):
        # XOR current element with next element
        arr[i] = arr[i] ^ arr[i + 1]
    
    # Last element remains unchanged
    return arr

