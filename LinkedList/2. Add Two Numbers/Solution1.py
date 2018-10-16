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
        while cur1.next and cur2.next:          #make up 0 ahead of the smaller num
            cur1 =cur1.next
            cur2 =cur2.next
        if not cur1.next:
            while cur2.next:
                cur1.next =ListNode(0)
                cur1 =cur1.next
                cur2 =cur2.next
        else:
            while cur1.next:
                cur2.next =ListNode(0)
                cur2 =cur2.next
                cur1 =cur1.next
            
        res =ListNode(0)
        cur =res
        carry =0
        cur1,cur2 =l1,l2
        while cur1:                             #addition operation
            tmp =cur1.val +cur2.val+carry
            cur.next =ListNode((tmp)%10)
            carry =(tmp)//10
            cur =cur.next
            cur1 =cur1.next
            cur2 =cur2.next
        if carry:                               #if carry,add 1 ahead of the res
            cur.next =ListNode(1)
    
        return res.next
    
                
                
        
            
        
            
        