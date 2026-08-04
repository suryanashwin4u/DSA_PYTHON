# You are given the head of a linked list and the number k, 
# You have to return the kth node from the end of linkedList. 
# If k is more than the number of nodes, then the return -1.

'''
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''

class Solution:
    def getKthFromLast(self, head, k):

        slow = head
        fast = head

        for _ in range(k):
            if fast is None:
                return -1
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        return slow.data