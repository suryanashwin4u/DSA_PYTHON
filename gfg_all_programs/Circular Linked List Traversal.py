# Given the head of a circular linked list, 
# print the data of the nodes in the linked list starting from the head node, 
# traversing the list exactly once.

# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def printList(self, head):
        if head is None:
            return

        curr = head
        while True:
            print(curr.data, end=" ")
            curr = curr.next
            if curr == head:
                break