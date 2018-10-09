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
        return self._reverse(head)
    
    def _reverse(self,node,pre=None):   #带pre默认参数
        if not node:                    #Terminal Condition
            return pre
        tmp =node.next                  #Internal Logic
        node.next =pre
      
        return self._reverse(tmp,node)  #Recursion Logic
