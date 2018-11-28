# 287. Find the Duplicate Number  

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.    

**Note:**

1.You must **not modify the array** (assume the array is read only).(means no sort)
2.You must use **only constant, O(1) extra space**.(means no new structure)
3.Your **runtime complexity should be less than O(n2)**.(means no brute force)
4.There is only one duplicate number in the array, but it could be repeated more than once.        

**Example 1:**  

Input: [1,2,3,4,2]
Output: 2     

**Example 2:**  

Input: [3,1,3,4,2]    
Output: 3       

## Ideas  
**idea 1**   
`Two pointers` (fast &slow)   
If consider the given array as a sort of linked list, it is the same as [142. Linked List Cycle II ](https://github.com/JingRachaelZhu/CrackLeetcode/tree/JingRachaelZhu-patch-1/LinkedList/142.%20Linked%20List%20Cycle%20II). A duplicate exists when a cycle does exist. Moreover, **the duplicate is the entry point of the cycle**(for eg1,its the second element `2`).So the key is to find the entry point of the cycle.     
1.The `fast` goes forward two steps each time, while the `slow` goes only step each time. They must meet within the cycle.   
2.Next,reset `fast` and move both pointers step by step until they meet at the entry point of the cycle.        

**NOTICE**         
* **How to convert into a linked list problem**: for eg1:1->2->3->4->2 ,then 2 back to 3to form a cycle.So If the duplicate exists ,then the cycle does exists as well.And because the two dups point to the same item,so the dup will be the entry point of the cycle.       
* **How to understand Step 2--find the entry point**:Since the `fast` go further than the slow,which the difference value is some multiplier of the loop length.Because the fast is twice faster than the slow, the diffrent value is exactly the diatance where slow goes from the start point to meeting point.This means, **the distance from start point to meeting point must be the n length of the loop length**.So when set another point starting from the start point and its speed is the same as the slow, if they walk a distance of n length of the loop, they will be at meeting point at the same time, so they must enter the loop at the same time. That's why the point where they first meet is the entry point of the loop.[see detail explain](https://leetcode.com/problems/linked-list-cycle-ii/discuss/44783/Share-my-python-solution-with-detailed-explanation)

* **Pay attention**:see Notice of [142. Linked List Cycle II ](https://github.com/JingRachaelZhu/CrackLeetcode/tree/JingRachaelZhu-patch-1/LinkedList/142.%20Linked%20List%20Cycle%20II).Here,`fast =0` means `fast` moves one step back.          

Time: O(n), Space: O(1)   

**idea 2**   
`Binary search`    
It is based on binary search.At first the search space is numbers between `1` to `n`. Each time I select a number `mid` (which is the one in the middle) and count all the numbers equal to or less than `mid`. Then if the count is more than mid, the search space will be [1, mid] otherwise [mid+1, n].(by [Pigeonhole Principle 鸽巢原理](https://en.wikipedia.org/wiki/Pigeonhole_principle) one of them has occurred more than once,then shrink the search range to [1, mid]),and repeat above step until `high` reach the dup.    

**NOTICE**      
* **How to come out such idea**:Since the range of items is [1,n] ,only one dup exists.Count the nums of items on half range help to shrink the search range .    
* **Binary search**: To prevent overflow,`mid =low +(high -low)//2`.when shrink the search range,should include the mid since counts `mid` in at above counting step,so`high=mid`other than `mid-1`.           

Time: O(logn), Space: O(1)     



