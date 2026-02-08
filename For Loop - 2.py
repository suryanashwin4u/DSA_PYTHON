# You are given a String S, you need to print its characters at even indices(index starts at 0).

def utility(s):
    # Traverse the string
    for i in range(len(s)):
        # Check if index is even
        if i % 2 == 0:
            print(s[i], end="")
