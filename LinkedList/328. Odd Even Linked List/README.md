# 328. Odd Even Linked List
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.  

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

**Example 1:**  

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL  

**Example 2:**  

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL

## Ideas  
**idea 1**   
`normal iteration`  
To solve it, divide the list into two lists,one is odd list,the other is even list.Then combine this two together to create the final list.  
1. First,initialize the `odd` to `head` and `even` to the `head.next` of the list.mark a `evenhead` for combination.  
2. while iterating the list,the `odd` will always points to the next odd position`second.next` and the `even` will point to the next even position `even.next.next`    
3. After completing the two list,merge this two list.The tail of odd list `odd.next` points to the `evenhead`  

**NOTICE**   
* **the edge case**: empty list or only have one item in the list.No change,return the list itself  
* **the terminal condition for while loop**: `even` and `even.next`is not None.    

Time: O(n), Space: O(1)      

 
