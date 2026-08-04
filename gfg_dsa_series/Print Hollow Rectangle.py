# Given two integers n and m, print a hollow rectangle pattern consisting of n rows and m columns.

# Time Complexity: O(n * m)
# Auxiliary Space: O(1)

n = int(input())                      # TC: O(1)  | SC: O(1)
m = int(input())                      # TC: O(1)  | SC: O(1)

for i in range(n):                    # TC: O(n)  | SC: O(1)
    for j in range(m):                # TC: O(m) per outer iteration | SC: O(1)
        if i == 0 or i == n-1 or j == 0 or j == m-1:
                                      # TC: O(1)  | SC: O(1)
            print("*", end="")        # TC: O(1)  | SC: O(1)
        else:
            print(" ", end="")        # TC: O(1)  | SC: O(1)
    print()                           # TC: O(1)  | SC: O(1)

# | Line        | Code                                           | Time Complexity              | Space Complexity |
# | ----------- | ---------------------------------------------- | ---------------------------- | ---------------- |
# | 1           | `n = int(input())`                             | **O(1)**                     | **O(1)**         |
# | 2           | `m = int(input())`                             | **O(1)**                     | **O(1)**         |
# | 3           | `for i in range(n):`                           | **O(n)**                     | **O(1)**         |
# | 4           | `for j in range(m):`                           | **O(m)** per outer iteration | **O(1)**         |
# | 5           | `if i == 0 or i == n-1 or j == 0 or j == m-1:` | **O(1)**                     | **O(1)**         |
# | 6           | `print("*", end="")`                           | **O(1)**                     | **O(1)**         |
# | 7           | `else:`                                        | **O(1)**                     | **O(1)**         |
# | 8           | `print(" ", end="")`                           | **O(1)**                     | **O(1)**         |
# | 9           | `print()`                                      | **O(1)**                     | **O(1)**         |
# | **Overall** | **Total Time Complexity**                      | **O(n × m)**                 | **O(1)**         |
