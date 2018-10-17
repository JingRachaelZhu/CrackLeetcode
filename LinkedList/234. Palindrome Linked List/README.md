# 234. Palindrome Linked List  

Given a singly linked list, determine if it is a palindrome.   

**Example 1:**  

Input: 1->2  
Output: false  

**Example 2:**  

Input: 1->2->2->1    
Output: true  

**Follow up:**
Could you do it in O(n) time and O(1) space?      


## Ideas  
**idea 1**   
`iteration` (reverse the first half) 
Because of the feature of palindrome, devide the list into two halves and compare the nodes of the two halves (one is reversed).  

**NOTICE**    
* **Edge case**: when list id None or only have one node,return True(it's palindrome)  
* **When comparing**:If the list have **odd** num of nodes,the first half should compare with the second half which starts with **mid+1** node(`slow` =`slow.next`)       

Time: O(n), Space: O(1)      

**idea 2**(more simple than `idea 1`,no deal with the odd-num-nodes list)       
`iteration` (reverse the second half)  
The same logic as `idea 1` while no special handling for odd-num-nodes list.    

Time: O(n), Space: O(1) 

