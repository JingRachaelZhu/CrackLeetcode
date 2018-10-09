# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy =ListNode(0)
        dummy.next=head
        pre =dummy
        for i in range(m-1):
            pre =pre.next

        cur =pre.next
        first_reverse =pre.next      #the first node of reverse part
        pre_reverse =None
        for i in range(n-m+1):
            tmp =cur.next
            cur.next =pre_reverse
            pre_reverse =cur
            cur =tmp
            
        first_reverse.next =cur     #link the head and tail of reverse part to the whole list
        pre.next =pre_reverse       
        
        return dummy.next
        
        
        
