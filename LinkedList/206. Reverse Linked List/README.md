# 206. Reverse Linked List
Reverse a singly linked list.

**Example 1:**  

Input: 1->2->3->4->5->NULL  
Output: 5->4->3->2->1->NULL

## Ideas  
**idea 1**   
`iteration`  
1. First,initialize the `pre` to None and `cur` to the `head` of the list.  
2. while iterating the list,the `pre` will always points to the former node before current node and the `cur.next` will point to the pre,which completes the invertion btn the two continuous node.  
3. After finishing the invertion,the `pre` will point to the current node and the `cur` will point to the next node.And do the same time above again until the `cur` reaches the end of the list(last node.next is None)

**NOTICE**    
* **Should return `pre` rather than head**: `pre` points to the original last node,which is the new first node now!! `Head` points to the orignal first node.  
* **if using oneline statement,order is still important**:`cur.next`,`cur`,`per` =`pre`,`cur.next`,`cur`, even though right-hand side is always evaluated fully before doing the actual setting of variables.  

Time: O(n), Space: O(1)      

**idea 2** (Less efficient than idea 1,cuz need more memory and time )   
`recursion`  
1. terminal condition: if current node is None,return None
2. recursive model : Similiar with `idea 1`, change last 2 statements into calling the function itself(apply recursion)  

Time: O(n), Space: O(n) 
