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
        isDuplicate =False
        while head:
            while head.next and head.val ==head.next.val:
                head.next =head.next.next
                isDuplicate =True
            if isDuplicate:                   #dups detected,skip dups
                pre.next =head.next
            else:                            #no dups,move forward
                pre =pre.next
            head =head.next
            isDuplicate =False              #reset mark as default value
        return dummy.next
        
