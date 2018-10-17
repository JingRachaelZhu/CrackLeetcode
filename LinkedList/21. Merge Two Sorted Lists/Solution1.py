# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
        if not l1 and not l2:   #edge case
            return None
        res =ListNode(0)
        dummy =res
        cur1 =l1
        cur2 =l2
        
        while cur1 and cur2:
            
            if cur1.val >= cur2.val:
                res.next =cur2
                cur2 =cur2.next
            else:
                res.next =cur1
                cur1 =cur1.next
            res =res.next
        
        if not cur1:                #edge case
            res.next =cur2
        if not cur2:
            res.next =cur1
        
              
        return dummy.nex
