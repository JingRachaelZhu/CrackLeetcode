# 80. Remove Duplicates from Sorted Array II

Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

**Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.**  
   

**Example 1:**  

Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.  

**It doesn't matter what you leave beyond the returned length.**  

**Example 2:**  

Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.  

It doesn't matter what values are set beyond the returned length.   

## Ideas  
**idea 1**   
`iteration` (reassign)   
It is similiar to [26. Remove Duplicates from Sorted Array](https://github.com/JingRachaelZhu/CrackLeetcode/tree/JingRachaelZhu-patch-1/Array/26.%20Remove%20Duplicates%20from%20Sorted%20Array) with the num of dups is 2.So when the num of dups is lees than 2, keep the value ,which is the same as when the comparing values are different.  

**NOTICE**      
* **Edge case**: when `nums` is None,return 0      
* **Set `mark` to record th num of dups: conclude that if the allowed dups is n, the mark should less than n while keep others the same as this pb does.**           

Time: O(n), Space: O(1)      

**idea 2** (another thinking)  
`iteration` (reassign)   
It will compare one item with the item 2 slots ahead.So copy the first two and start comparision from the third item.If one item is larger than the item 2 slots ahead,it means this item at most appears twice ,then keep it.


**NOTICE**      
* **Compare with the updated item**: When comparing the `num` with the item ahead, the item ahead should be **the updated one(`nums[ct-2]`)** rather than the original one in the array.        
           

Time: O(n), Space: O(1) 


