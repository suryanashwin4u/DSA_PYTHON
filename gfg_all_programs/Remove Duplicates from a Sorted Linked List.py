# Given a singly linked list. 
# The task is to remove duplicates (nodes with duplicate values) from the given list (if it exists).
# Note: Try not to use extra space. 
# The nodes are arranged in a sorted way.

def removeDuplicates(head):
    current = head
    
    while current and current.next:
        if current.data == current.next.data:
            # remove duplicate
            current.next = current.next.next
        else:
            current = current.next
            
    return head