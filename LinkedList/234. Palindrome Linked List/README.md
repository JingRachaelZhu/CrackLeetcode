# 21. Merge Two Sorted Lists  

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.(in order)  

**Example 1:**  

Input: 1->2->4, 1->3->4  
Output: 1->1->2->3->4->4  

## Ideas  
**idea 1**   
`iteration`  
It is a basic merge problem .Need to compare nodes of two lists before merge them together.
For example, if `cur1.val` >= `cur2.val`, `res.next` store `cur2` ,then `res` and `cur2` moves forward(`res.next`,`cur2.next`)  


**NOTICE**    
* **edge case**: when both lists is None,return None.When either is None,return the other one.        

Time: O(n), Space: O(n)      

**idea 2** ( more elegant version)   
`recursion`   
The same logic as `idea 1` while code looks more elegant.  

Time: O(n), Space: O(n) 

