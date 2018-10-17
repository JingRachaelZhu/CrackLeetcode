# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """ 
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val >= l2.val:
            l2.next =self.mergeTwoLists(l1, l2.next)   #l2 moves forward
            return l2
        else:
            l1.next =self.mergeTwoLists(l1.next, l2)   #l1 moves forward
            return l1
            
        