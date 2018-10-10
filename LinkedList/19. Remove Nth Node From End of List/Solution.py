# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next :     #eadge case
            return []
        pre =ListNode(0)
        pre.next =head
        fast =pre
        slow =pre
        for i in xrange(n+1):             #move n+1 forwad, keep n+1 gap of two vals
            fast =fast.next
            
        while fast:
            slow =slow.next
            fast =fast.next
        slow.next =slow.next.next       
        return pre.next
            
