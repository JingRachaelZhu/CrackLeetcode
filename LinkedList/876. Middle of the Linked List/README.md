# 876. Middle of the Linked List
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

**Example 1:**  
Input: [1,2,3,4,5]  
Output: Node 3 from this list (Serialization: [3,4,5])  
**Example 2:**  
Input: [1,2,3,4,5,6]  
Output: Node 4 from this list (Serialization: [4,5,6])  

## Ideas  
**idea 1**   
`normal iterating the list 1.5 times`  
1. First,get the length of the linked list by iterating the whole lined list.  
2. Then define a val called `cur` that pointing to the head of the linked list, then iterating the linked list until the `cur` reaches the mid position.  

Time: O(n), Space: O(1)      

**idea 2**(More efficient than idea 1,cuz only need to iterate the list 1 time)   
`Fast/Slow Pointers`  
1. First,initialize two pointers `Fast` and `Slow` ,both point to `head`.  
2. Iterate the whole linked list.Each time, `Fast` will reach 2 step away while `Slow` will reach one step.
3. Finally, when `Fast` reach the end of the list, `Slow` will reach right in the mid position.  

Time: O(n), Space: O(1) 
