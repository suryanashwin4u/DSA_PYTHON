# Given the head of a linked list, determine whether the list contains a loop. 
# If a loop is present, return the number of nodes in the loop, otherwise return 0.
# Note: Internally, pos(1 based index) is used to denote the position of the node that tail's next pointer is connected to. 
# If pos = 0, it means the last node points to null, indicating there is no loop. 
# Note that pos is not passed as a parameter.

# Time Complexity: O(n)
# Auxiliary Space: O(1)

'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, head):
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                count = 1
                temp = slow.next

                while temp != slow:
                    count += 1
                    temp = temp.next

                return count

        return 0