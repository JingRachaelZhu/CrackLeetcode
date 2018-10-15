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
        #Tricky 
        cur =head
        NonNine =None
        while cur:               #find the least significant non-9 dight
            if cur.val !=9:
                NonNine =cur
            cur =cur.next     

        if not NonNine:			    #case: all num on digits are 9
            NonNine =ListNode(1)
            NonNine.next =head
            head =NonNine
        else:
            NonNine.val +=1

        NonNine.next =restNines	 #set all rest 9 to 0 
        while restNines:
            restNines.val =0
            restNines =restNines.next

        return head
