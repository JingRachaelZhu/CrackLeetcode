# 189. Rotate Array 

Given an array, rotate the array to the right by k steps, where k is non-negative.      

**Example 1:**  

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]   

**Example 2:**  

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]   

**Note:**

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?      

## Ideas  
**idea 1**   
`iteration`(straightforward)    
It does as the topic described.First of all,need to evaluate the value of `k`,the effective part is the remainder.Then pop item fro the end and insert it at the head `k` times.   
  
**NOTICE**      
* **Edge case**: when `nums` is `None` ,return     
* **Evaluate the value of `k`**:If `k` id greater than the lengh of array,reassign thr remainder to `k`,which is the exact num of the steps for operation.              

Time: O(n), Space: O(1)      

**idea 2**(more simple)   
`iteration`(Slice assignment)       
It mainly devides the whole array into two part in term of k. and put second part ahead of first part to join them together to form the result.
  
**NOTICE**      
* **Time complexity**: Get slice is O(n).       
* **Evaluate the value of `k`**:If `k` id greater than the lengh of array,reassign thr remainder to `k`,which is the exact num of the steps for operation.              

Time: O(n), Space: O(1) 

