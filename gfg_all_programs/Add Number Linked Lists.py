# You are given the head of two singly linked lists head1 and head2 representing two non-negative integers. You have to return the head of the linked list representing the sum of these two numbers.

# Note: There can be leading zeros in the input lists, but there should not be any leading zeros in the output list.

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def reverse(self, head):
        prev = None
        curr = head
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        return prev

    def addTwoLists(self, head1, head2):
        # Step 1: Reverse both lists
        head1 = self.reverse(head1)
        head2 = self.reverse(head2)

        carry = 0
        dummy = Node(0)
        curr = dummy

        # Step 2: Add
        while head1 or head2 or carry:
            sum_val = carry

            if head1:
                sum_val += head1.data
                head1 = head1.next

            if head2:
                sum_val += head2.data
                head2 = head2.next

            carry = sum_val // 10
            curr.next = Node(sum_val % 10)
            curr = curr.next

        # Step 3: Reverse result
        result = self.reverse(dummy.next)

        # Step 4: Remove leading zeros
        while result and result.data == 0 and result.next:
            result = result.next

        return result
        