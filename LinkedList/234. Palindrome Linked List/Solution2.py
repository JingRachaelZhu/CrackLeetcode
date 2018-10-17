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
       
        pre =None                           #reverse second half
        while slow:
            tmp =slow.next
            slow.next =pre
            pre =slow
            slow =tmp
            
        cur =head                          #compare nodes of two halves
        while pre and cur:
            if pre.val !=cur.val:
                return False
            pre =pre.next
            cur =cur.next
            
        return True