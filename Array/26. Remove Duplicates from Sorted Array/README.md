# 26. Remove Duplicates from Sorted Array  

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

**Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.**      

**Example 1:**  

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

**It doesn't matter what you leave beyond the returned length.**   

**Example 2:**  

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.    

## Ideas  
**idea 1**   
`iteration` (reassign)   
It is similar to [27. Remove Element ](https://github.com/JingRachaelZhu/CrackLeetcode/tree/JingRachaelZhu-patch-1/Array/27.%20Remove%20Element). If     

**NOTICE**      
* **Edge case**: when list id None or only have oneor two node,return    
* **After finding mid node(`slow`)**:The `slow.next` will be the beginning of the `sec_half`.`slow` will be the last node of the result,so `slow.next` =`None`.           

Time: O(n), Space: O(1)      



