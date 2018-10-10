# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:return head
        head.next =self.removeElements(head.next,val)
        if head.val == val:
            return head.next
        else:
            return head
    
        
