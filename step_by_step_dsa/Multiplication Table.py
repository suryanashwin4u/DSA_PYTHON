# Given a number n, print the multiplication table from 1 to 10 for n in a single line, separated by spaces.
# Expected Complexities
# Time Complexity: O(1)
# Auxiliary Space: O(1)

n = int(input())

# Loop from 1 to 10 and print each multiple separated by a space
for i in range(1, 11):
    print(n * i, end=" ")