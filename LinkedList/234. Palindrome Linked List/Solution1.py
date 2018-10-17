# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:       #edge case
            return True
        
        slow =head                          #find mid node
        fast =head
        while fast and fast.next:
            fast =fast.next.next
            slow =slow.next
        mark =slow
        if fast:                #odd num,second helf startes one more further
            slow =slow.next
            
        cur =head               #reverse first half
        pre =None
        while cur !=mark:
            tmp =cur.next
            cur.next =pre
            pre =cur
            cur =tmp
            
        while pre and slow:     #compare nodes of two halves
            if pre.val != slow.val:
                return False
            pre =pre.next
            slow =slow.next
            
        return True
        