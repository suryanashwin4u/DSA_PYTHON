# Given two integers n and m, print a solid rectangle pattern of n rows and m columns using the "*" character.

# Note: There is a space between two adjacent stars (*) in the pattern.

# Time Complexity: O(n*m)
# Auxiliary Space: O(1)

n = int(input())                # TC: O(1), SC: O(1)
m = int(input())                # TC: O(1), SC: O(1)

# Outer loop runs n times
for i in range(n):              # TC: O(n), SC: O(1)

    # Inner loop runs m times for each row
    for j in range(m):          # TC: O(n × m), SC: O(1)
        print("*", end=" ")     # TC: O(1), SC: O(1)

    print()                     # TC: O(1), SC: O(1)

# | Line | Code                  | Time Complexity        | Space Complexity |
# | ---- | --------------------- | ---------------------- | ---------------- |
# | 1    | `n = int(input())`    | **O(1)**               | **O(1)**         |
# | 2    | `m = int(input())`    | **O(1)**               | **O(1)**         |
# | 4    | `for i in range(n):`  | **O(n)** iterations    | **O(1)**         |
# | 5    | `for j in range(m):`  | **O(n × m)** total     | **O(1)**         |
# | 6    | `print("*", end=" ")` | **O(1)** per execution | **O(1)**         |
# | 7    | `print()`             | **O(1)** per row       | **O(1)**         |
