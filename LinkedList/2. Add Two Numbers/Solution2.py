# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur1,cur2 =l1,l2
        res =ListNode(0)
        cur =res
        carry =0                      
        while cur1 or cur2 or carry:
        	if cur1:
        		carry +=cur1.val            #`carry` store the sum
        		cur1 =cur1.next
        	if cur2:						
        		carry +=cur2.val
        		cur2 =cur2.next
        	cur.next =ListNode(carry%10)
        	cur =cur.next
        	carry =carry//10				#0 or 1
        return res.next
