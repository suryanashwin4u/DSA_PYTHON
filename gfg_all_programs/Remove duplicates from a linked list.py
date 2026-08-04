# Given an unsorted linked list. 
# The task is to remove duplicate elements from this unsorted Linked List. 
# When a value appears in multiple nodes, the node which appeared first should be kept, all other duplicates are to be removed.

'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None	
'''

class Solution:
    # Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        if head is None:
            return head
        
        seen = set()
        curr = head
        prev = None
        
        while curr:
            if curr.data in seen:
                # duplicate → remove node
                prev.next = curr.next
            else:
                seen.add(curr.data)
                prev = curr
            
            curr = curr.next
        
        return head