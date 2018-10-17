# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:       #edge case
            return
        fast =head                          #find the mid node
        slow =head
        while fast and fast.next:
            fast =fast.next.next
            slow =slow.next
            
        rev =slow.next                      #reverse second half:4->5 --->5->4
        slow.next =None                     #slow will be the last node of the result
        pre =None
        while rev:
            tmp =rev.next
            rev.next =pre
            pre =rev
            rev =tmp
            
        sec_half =pre                      #combine two halves
        cur =head
        while sec_half:                    #1->2->3,5->4
            tmp1 =cur.next                 #loop1:1->5->2,loop2:2->4->3
            cur.next =sec_half
            tmp2 =sec_half.next
            sec_half.next =tmp1
            cur =tmp1
            sec_half =tmp2
        