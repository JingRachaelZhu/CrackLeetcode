# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:return head
        dummy =ListNode(0)
        dummy.next =head
        pre =dummy
        cur =head
        while cur:
            while cur.next and cur.val ==cur.next.val:
                cur =cur.next                            #move cur to the last node of duplicates
                
            if pre.next ==cur:                          #no dups detected,move forward
                pre =pre.next
            else:
                pre.next =cur.next                     # skip the dups for pre
                
            cur =cur.next
        return dummy.next
        
