# Geek is very fond of patterns. 
# Once, his teacher gave him a square pattern to solve. 
# He gave Geek an integer n and asked him to build a pattern.
# Help Geek to build a square pattern with the help of *  such that each * is space-separated in each line.

class Solution:
    def printSquare(self, N):
        # Loop for rows
        for i in range(N):
            # Loop for columns
            for j in range(N):
                print("* ", end="")  # print star with space, stay on same line
            print()  # move to next line after each row

