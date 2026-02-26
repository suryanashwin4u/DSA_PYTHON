# You are given a singly linked list of n elements, 
# and also an element x. 
# You need to find if x is present in the linked list or not. 
# Return true if x is present else returns false. 
# (1 is printed by the driver code if the returned value is true, otherwise 0)

class Solution:
    def searchLinkedList(self, head, x):
        current = head
        
        while current is not None:
            if current.data == x:
                return True
            current = current.next
        
        return False