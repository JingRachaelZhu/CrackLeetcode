# 24. Swap Nodes in Pairs  
Remove all elements from a linked list of integers that have value val.

**Example 1:**    

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5  

## Ideas  
**idea 1**   
`iteration`  
It has the same way as [`83. Remove Duplicates from Sorted List`](https://github.com/JingRachaelZhu/CrackLeetcode/tree/JingRachaelZhu-patch-1/LinkedList/83.%20Remove%20Duplicates%20from%20Sorted%20List)     
1. First,initialize `dummy` to ahead of the `head` and `cur` points to `dummy`(case: the `head` is the target node)    
2. while iterating the list,if `cur.next.val` equals to `val`,`cur.next` will point to the next node of `cur.next`      
3. Finally, return dummy.next  

**NOTICE**  
* **edge case**: if empty list , return itself.  
* **Should return `dummy.next`**: `dummy.next` always points to the head of the list. `head`only points to the original first node.     

Time: O(n), Space: O(1)      

**idea 2** (Less efficient than idea 1,cuz need more memory and time )   
`recursion`  
1. terminal condition: if current node `head` is None,return head  
2. internal logic:  if `head.val` equals to `val`,return next node,else return `head` itself.   
3. recursive logic: the current node `head.next` will points to the return val of the next recursion  

Time: O(n), Space: O(n) 
