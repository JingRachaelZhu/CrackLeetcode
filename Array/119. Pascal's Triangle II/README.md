# 119. Pascal's Triangle  II  

Easy,seldom ask 

## Ideas  
**idea 1**   
Find the rule .The trick here is to find the pattern that each row's [i]th index is actually **the sum of [i] and [i-1] of the previous row**. Note: each row will increase by 1 number length, that new element defaults to 0, those values are bold in the above example.   

**NOTICE**      
* **Edge case**: when `numRows` is 0 ,return []      
* **the * operation in list**:         

Time: O(n^2), Space: O(n) 