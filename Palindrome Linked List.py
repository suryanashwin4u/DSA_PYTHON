# You are given the head of a singly linked list of positive integers. 
# You have to check if the given linked list is palindrome or not.

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    def isPalindrome(self, head):
        # Edge case
        if head is None or head.next is None:
            return True
        
        # Step 1: Find middle (slow-fast)
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse second half
        prev = None
        curr = slow
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # Step 3: Compare both halves
        first = head
        second = prev
        
        while second:
            if first.data != second.data:
                return False
            first = first.next
            second = second.next
        
        return True
        