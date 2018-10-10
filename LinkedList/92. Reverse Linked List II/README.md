# 92. Reverse Linked List II
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

**Example 1:**    

Input: 1->2->3->4->5->NULL, m = 2, n = 4  
Output: 1->4->3->2->5->NULL  

## Ideas  
**idea 1**   
`iteration reverse`  
It is a part-reverse problem.Reverse part of the list.Still Set a node `dummy` in front of the head.Need to reach to the reverse part       
1. First,initialize the `pre` to `dummy` and iterating the list until `pre` reaches the node ahead of the reverse list.     
2. Then,Start reversing the nodes among the n-m part of the list.Same way as [`206. Reverse Linked List`](https://github.com/JingRachaelZhu/CrackLeetcode/tree/JingRachaelZhu-patch-1/LinkedList/206.%20Reverse%20Linked%20List)     
3. At last, link the `pre` node to the new `first node` of the reversed part and link the new `tail node` of reversed part to the next node in the whole list 


**NOTICE**    
* **Should return `dummy.next` rather than `head`**: `dummy.next` always points to the head of the list while the `head` in some cases(when m=1)will no longer be the head of the new list.     
* **Pay attention to the range for each loop**  

Time: O(n), Space: O(1)      

