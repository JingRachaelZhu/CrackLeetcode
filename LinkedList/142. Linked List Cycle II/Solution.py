# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow =head
        fast =head
        while fast and fast.next:
            slow =slow.next
            if not fast.next:return None    #no cycle
            fast =fast.next.next
            if fast ==slow:break
            
        if not fast or not fast.next:       #no cycle
            return None
        fast =head                          #find the entry point
        while fast !=slow:
            slow =slow.next
            fast =fast.next
            
        return slow