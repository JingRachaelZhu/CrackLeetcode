# 142. Linked List Cycle II  

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.          

**Note:** Do not modify the linked list.  

**Follow up:**
Can you solve it without using extra space?          

## Ideas  
**idea 1**   
`Two pointers` (fast &slow)  
It is the same idea as `idea 1` of [287. Find the Duplicate Number](https://github.com/JingRachaelZhu/CrackLeetcode/tree/JingRachaelZhu-patch-1/Array/287.%20Find%20the%20Duplicate%20Number).Use `Fast&slow` to find the crossing point.Next step is the key --- to find the entry point.

**NOTICE**      
* **How to find the entry point**:The distance [see detail explain](https://leetcode.com/problems/linked-list-cycle-ii/discuss/44783/Share-my-python-solution-with-detailed-explanation)  
* **Pay attention**:If `fast` and `slow` both start from `head`,then step2 should reset `fast` to `head`(`fast =head`).If `slow` starts from `head` while `fast` starts from `head.next`,then step2 should either move `slow` one step forward(`slow =slow.next`) while fast still start from `head`(`fast =head`) or `fast` move one step back(`fast =dummy`,where `dummy =ListNode(0)`,`dummy.next =head`).            
Time: O(n), Space: O(1)      



