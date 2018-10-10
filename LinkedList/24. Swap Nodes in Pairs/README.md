# 24. Swap Nodes in Pairs  
Given a linked list, swap every two adjacent nodes and return its head.

**Example 1:**    

Given 1->2->3->4, you should return the list as 2->1->4->3.

## Ideas  
**idea 1**   
`iteration`  
It is a sub-reverse problem.Every two adjacent nodes exchange place with each other.Set a node `dummy` in front of the head: `dummy->1->2->3->4`,change to `dummy->2->1->4->3`   
1. First,initialize `cur` to the `dummy`    
2. while iterating the list,first points to the first node of two,second points to the second one.(the terminal condintion is there are no more than two nodes)  
3. To change the order,need to modify 3 things.`dummy->1->2` change to `dummy->2->1`  
4. After finishing the invertion, get `cur` reach to the node ahead of the next two nodes  

**NOTICE**    
* **Should return `pre.next`**: `pre.next` points to the `head` of the list.    

Time: O(n), Space: O(1)      

**idea 2** (Less efficient than idea 1,cuz need more memory and time )   
`recursion`  
1. terminal condition: if current node `head` or next node `head.next` is None,return head  
2. internal logic: the `second.next` points to the `head` node(which is the current node).`1->2` change to `2->1`  
3. recursive logic: the current node `head.next` will points to the return val of the next recursion  

Time: O(n), Space: O(n) 
