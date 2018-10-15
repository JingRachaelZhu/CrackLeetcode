# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #stack
        stack =[]
        cur =head
        while cur:
            stack.append(cur)
            cur =cur.next

        carry =1
        pre =None
        res =ListNode(0)
        while stack :
            cur =stack.pop()
            res.val =(cur.val+carry)%10
            carry =(cur.val+carry)//10
            res.next =pre     	# reverse order
            pre =res

        if carry:
            res =ListNode(1)
            res.next =pre
            
        return res
