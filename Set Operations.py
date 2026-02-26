# You are given an array arr[] of size n. 
# You have to insert all elements of arr[] into a set and return that set.
# You are also given a interger x. 
# If x is found in set then erase it from set and print "erased x", 
# otherwise, print "not found".
# Note: Only complete setDisplay() method, 
# do not print the set yourself — the driver will handle printing.

def setInsert(arr, n):
    return set(arr)

def setDisplay(s):
    for i in sorted(s):
        print(i, end=" ")
    print()

def setErase(s, x):
    if x in s:
        s.remove(x)
        print("erased", x)
    else:
        print("not found")