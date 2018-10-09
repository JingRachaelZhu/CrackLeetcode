# 141. Linked List Cycle
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?


## Ideas  
**idea 1**   
`Fast/Slow pointers`  
1. First,initialize two pointers `Fast` and `Slow` ,both point to `head`.  
2. Iterate the whole linked list.Each time, `Fast` will reach 2 step away while `Slow` will reach one step.
3. Finally, if the linked list has a cycle, the `Fast` will meet the `Slow` at some point. If not, when the `Fast` reaches the end of the list(pointing to None finally),retuen `False`.     

**NOTICE**    
* **No extra space usually means costant space** 

Time: O(n), Space: O(1)      

