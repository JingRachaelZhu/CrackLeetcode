# 83. Remove Duplicates from Sorted List
Given a sorted linked list, delete all duplicates such that each element appear only once.

**Example 1:**  
Input: 1->1->2  
Output: 1->2

**Example 2:**  
Input: 1->1->2->3->3  
Output: 1->2->3

## Ideas  
**idea 1**   
`normal iteration`  
1. First,initialize the `cur` to the `head` of the list    
2. Then iterating the list,if two adjacent nodes have the same value, the first node linked to the next node of second node.`cur.next` =`cur.next.next`     

**NOTICE**   
* **the edge case**: empty list or only have one item in the list.No change,return the list itself  

Time: O(n), Space: O(1)      
 
