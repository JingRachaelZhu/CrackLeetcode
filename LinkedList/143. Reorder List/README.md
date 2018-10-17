# 143. Reorder List  

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…  

You may **not** modify the values in the list's nodes, only nodes itself may be changed.     

**Example 1:**  

Given 1->2->3->4, reorder it to 1->4->2->3.  

**Example 2:**  

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.    

## Ideas  
**idea 1**   
`iteration` (find mid,reverse the second half)   
It is similar to [234. Palindrome Linked List ](https://github.com/JingRachaelZhu/CrackLeetcode/tree/JingRachaelZhu-patch-1/LinkedList/234.%20Palindrome%20Linked%20List) use fast/slow to find the mid node and reverse the second half of the list.Then, add nodes as the problem requests.   

**NOTICE**      
* **Edge case**: when list is `None` or only have one or two node,return    
* **After finding mid node(`slow`)**:The `slow.next` will be the beginning of the `sec_half`.`slow` will be the last node of the result,so `slow.next` =`None`.           

Time: O(n), Space: O(1)      



