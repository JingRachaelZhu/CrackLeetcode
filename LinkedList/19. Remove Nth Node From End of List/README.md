# 9. Remove Nth Node From End of List  
Given a linked list, remove the n-th node from the end of list and return its head.

**Example 1:**    

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.  

**Note:**

Given n will always be valid.

**Follow up:**

Could you do this in one pass?

## Ideas  
**idea 1 One pass solution**  
`Fast/slow pointer`  
It is a `Fast/slow ponter` problem. the similar way as [`876. Middle of the Linked List`](https://github.com/JingRachaelZhu/CrackLeetcode/tree/JingRachaelZhu-patch-1/LinkedList/876.%20Middle%20of%20the%20Linked%20List)    
1. First,define a `pre` in ahead of the head of the list,in case the target node is the head node. `fast` and `slow` point to `pre`        
2. Move the `fast` n places forward, to maintain a gap of n between `fast` and `slow`    
3. Then move both two at the same speed until the `fast` reaches the end of the list,the `slow` will be n places behind - just the right spot for it to be able to skip the next node.   

**NOTICE**    
* **check `n` if not mention it's valid**: Since the question gives that `n` is valid, not too many checks have to be put in place. Otherwise, this would be necessary.    

Time: O(n), Space: O(1)      

