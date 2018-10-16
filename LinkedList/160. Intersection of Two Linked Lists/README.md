# 160. Intersection of Two Linked Lists  

Write a program to find the node at which the intersection of two singly linked lists begins.

**Example 1:**  

For example, the following two linked lists:

A:          a1 → a2
                 ↓   
                 c1 → c2 → c3  
                 ↑               
B:     b1 → b2 → b3  
begin to intersect at node c1.  

**Notes:**

* If the two linked lists have no intersection at all, return null.
* The linked lists must retain their original structure after the function returns.
* You may assume there are no cycles anywhere in the entire linked structure.
* Your code should preferably run in O(n) time and use only O(1) memory.

## Ideas  
**idea 1**   
`iteration`  
It is similar to [19. Remove Nth Node From End of List](https://github.com/JingRachaelZhu/CrackLeetcode/tree/JingRachaelZhu-patch-1/LinkedList/19.%20Remove%20Nth%20Node%20From%20End%20of%20List).The longer one needs to reach specific positon so that it will remain the same distance away from the target node as the short one when moving forward.  
1. First, compare the lenghths of two lists  
2. Then,deal with the longer list, make `cur(1/2)` reach the specific position to keep the same pace as the short one while moving forward.(The same distance away from the target node) 
3. Finally, compare each node of two list

**NOTICE**    
* **abs()funtion**: return the abslute value of argument.eg.`dif` =`ads(num1-num2)`  
* **When some duplicates happen in coding**: try to integrate it or create funtion for it.    

Time: O(n), Space: O(1)      

**idea 2** ( more tricky version)   
`iteration`   
Using `A` linked `B`,`B` linked `A` to fill up the diff of the two length.When the two `cur1` and `cur2` meet each other,it is right on the target node.(cuz the two vals go through the same distance when they meet) 
eg.  2    4  
      +2    +2(right here when the  `cur1` and `cur2` meet)  
     4    2


Time: O(n), Space: O(1) 

