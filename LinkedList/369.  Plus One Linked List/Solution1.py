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
	      #normal reverse
        def reverse(node):
            pre =None
            while node:
                tmp =node.next
                node.next =pre
                pre =node
                node =tmp
            return pre

      h2 =reverse(head)
      rev1 =h2
      while rev1:
          if rev1.val+1 >9 :
              rev1.val =0
              if not rev1.next:
                  rev1.next =ListNode(1)
                  break
          else :
              rev1.val +=1
              break
          rev1 =rev1.next

      res =reverse(h2)
      return res
