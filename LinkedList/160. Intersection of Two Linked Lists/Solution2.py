# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        cur1 =headA
        cur2 =headB
        while cur1 != cur2:							#use A linked B,B linked A to fill up the diff of two lengths
        	cur1 =headB if not cur1 else cur1.next
        	cur2 =headA if not cur2 else cur2.next

        return cur1



        
