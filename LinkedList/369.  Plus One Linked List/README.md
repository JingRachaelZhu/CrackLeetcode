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
`iteration`(normal)  
reverse,addition,reverse.       
1. First,define the reverse funtion. the same way as [206. Reverse Linked List](https://github.com/JingRachaelZhu/CrackLeetcode/tree/JingRachaelZhu-patch-1/LinkedList/206.%20Reverse%20Linked%20List)     
2. Then,additon operation
3. Finally, reverse again

**NOTICE**    
* **Pay attention to variable change**     

Time: O(n), Space: O(1)   

**idea 2**   
`stack`   
using the feature of stack---FILO, deal with the node from the end.       
1. First,push value of each node into stack (1,2,9)  
2. Then, pop values from the end of stack (9,2,1)to do the plus 1 operation.(`val` = (`val`+`carry`)%10, `carry` = (`val`+`carry`)//10) 
3. Finally, if `carry` is 1,add one more digit ahead of the list  

**NOTICE**    
* **Step 2**: deal with the num from the end,so **reverse order** when linking two nodes.      

Time: O(n), Space: O(n)

**idea 3** (**This method coould be applied to similiar addition problems**)   
`iteration`（Tricky）  
Use `NonNine` to track the last non 9 digit position. If all digits are 9, add 1 ahead of the list.If not,add 1 to `NonNine`.Finally, set the rest 9s to 0.    
1. First, find the least significant non-9 digit  
2. Then,deal with the `NonNine`.Case1, `NonNine` doesnt exist (all digits are 9s). Case2, `NonNine` exists.  
3. Finally, set all the rest 9s to 0.   

Time: O(n), Space: O(1) 
