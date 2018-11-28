# 142. Linked List Cycle II  

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.         

**Example 1:**  

Input: [1,3,4,2,2]
Output: 2     

**Example 2:**  

Input: [3,1,3,4,2]    
Output: 3       

## Ideas  
**idea 1**   
`Two pointers` (fast &slow)  
   

**NOTICE**      
* **Edge case**: when list id None or only have oneor two node,return    
* **After finding mid node(`slow`)**:The `slow.next` will be the beginning of the `sec_half`.`slow` will be the last node of the result,so `slow.next` =`None`.           

Time: O(n), Space: O(1)      



