# 369. Plus One Linked List  
Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.
You may assume the integer do not contain any leading zero, except the number 0 itself.
The digits are stored such that the most significant digit is at the head of the list.

**Example 1:**    

Input:
1->2->3

Output:
1->2->4

## Ideas  
**idea 1**   
`iteration`  
Normally, it can be solved by adding a internal funtion `reverse()`.reverse it at the beginning ,after finishing the addtion，reverse it back at last.     
1. First,   
2. Then
3. Finally, 

**NOTICE**    
* **Should return `pre.next`**:     

Time: O(n), Space: O(1)      

**idea 2** (**This method coould be applied to similiar addition problems**)   
`iteration`  
Use two pointer, j to travel the linkedlist, i to track the last non 9  digit position.
Add 1 to i, and set the rest digits 0.    
1. First,   
2. Then
3. Finally, 

Time: O(n), Space: O(1) 
