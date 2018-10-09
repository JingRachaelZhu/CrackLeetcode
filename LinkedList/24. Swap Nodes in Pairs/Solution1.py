# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre =ListNode(0)
        pre.next =head
        cur =pre
        while cur.next and cur.next.next:
            first =cur.next
            second =cur.next.next
            cur.next =second
            first.next =second.next
            second.next =first
            cur =first
        return pre.next
