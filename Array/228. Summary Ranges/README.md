# 228. Summary Ranges              


Given a sorted integer array without duplicates, return the summary of its ranges.              

## Ideas  
**idea 1**   
`count`    
It is a problem to devide nums into several ranges. The key is to skip the continuous nums and find the gap.Set a variable `start` to mark the startpoint of the range.                 

**NOTICE**      
* **When the adjacent nums are continuous**:Use while loop to skip to next num.      
* **The two conditions**:If `start`==nums[i], means it has **only one num** in this range.If not, means there is at least two nums in this range.                 

Time: O(n), Space: O(1)           



