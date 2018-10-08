# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        leng =0
        cur =head
        while cur:
            leng +=1
            cur =cur.next
        cur =head
        mid = leng//2
        while mid >0:
            mid -=1
            cur =cur.next

        return cur
            
       
        
            
