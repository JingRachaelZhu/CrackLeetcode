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
        def length(linkedlist):
            ct =0
            cur =linkedlist
            while cur:
                ct +=1
                cur =cur.next
            return ct
        dif =abs(length(headA)-length(headB))
        cur1 =headA
        cur2 =headB
        if length(headA)>length(headB):   		#track the longer one until it remains the same num of nodes as shorter one 
            for i in range(dif):
                cur1 =cur1.next
        else:
            for i in range(dif):
                cur2 =cur2.next
                
        while cur1 != cur2:  					#compare each node of two lists
            cur1 =cur1.next
            cur2 =cur2.next
           
        return cur1

        
        
            
        
        
