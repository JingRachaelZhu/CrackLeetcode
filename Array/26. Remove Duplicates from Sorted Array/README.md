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
It is similar to [27. Remove Element ](https://github.com/JingRachaelZhu/CrackLeetcode/tree/JingRachaelZhu-patch-1/Array/27.%20Remove%20Element). SOTRED ARRAY is the key.Since it's sorted, should compare with pairs each time. Once find the target value,assign it to `nums[ct]`(`ct` starts from `1`, which is different from `pb27. Remove Element`).       

**NOTICE**      
* **Edge case**: when `nums` is None,return 0      
* **`ct` starts from `1`**:Since the aim of this pb is to remove the dups in sorted array.When find the dup of first item ,reassign next different value to the dup without operating first item .So always keep thr first item.          

Time: O(n), Space: O(1)      


