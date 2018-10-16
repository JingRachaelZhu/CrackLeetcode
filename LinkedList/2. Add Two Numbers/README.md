# 2. Add Two Numbers 

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.  

**Example 1:**    

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.  

## Ideas  
**idea 1**   
`iteration`  
It is much easier than [369. Plus One Linked List](https://github.com/JingRachaelZhu/CrackLeetcode/tree/JingRachaelZhu-patch-1/LinkedList/369.%20%20Plus%20One%20Linked%20List),since the head is the least significant digit. Pay attention to compare the num of the digits of two nums with each other. 
1. First, make up `0` to the smaller nums ,so that both of them have the same num of digits.   
2. Then,addition operation
3. Finally,if the carry is `1`, add one more `1` ahead of the `res` list.   

**NOTICE**    
* **No need to reverse**:eg. `res.next` =ListNode(0),`res` =`res.next`
* **Don‘t forget to handle the last `carry`**: if `carry`, add 1 ahed of the result.       

Time: O(n), Space: O(n)(create new list)      

**idea 2** (more clear and simple version,similar logic)  
`iteration`
The most smart tip is the `carry` part.`carry` will store the sum for l1 and l2(or either one).then in the end of each loop, `carry` =`carry` //10 ,means the carry for next addition.No need to make up `0` any more,since `carry` will be either `0` or `1`(always valid).  

Time: O(n), Space: O(n)(create new list)
