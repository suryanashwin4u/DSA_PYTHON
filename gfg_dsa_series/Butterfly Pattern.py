# Given a number n. Print Butterfly Pattern with n lines. 

# Time Complexity: O(n^2)
# Auxiliary Space: O(1)

n = int(input())

# The pattern has (2 * n - 1) rows in total
for i in range(1, 2 * n):
    # Calculate stars on each wing for the current row
    stars = i if i <= n else 2 * n - i
    
    # Calculate middle spaces
    spaces = (2 * n - 1) - (2 * stars)
    
    if spaces <= 0:
        # Middle row has no spaces
        print("*" * (2 * n - 1))
    else:
        print("*" * stars + " " * spaces + "*" * stars)