# 152. Maximum Product Subarray         

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.          



## Ideas  
**idea 1**   
`Kadane’s Algorithm`    
It is similar to 53. Maximum Subarray.The difficult part is how to deal with the `current max` with negative num.We need to `track mancur and mincur` at the same time.When we encounter a negative num,we could use `mincur * negative` to get the mac cur.  

**NOTICE**      
* **How to deal with current product with negative num**: Since the num is negative,we can swap `maxcur` with `maxmin`.   
* **Find the maxcur**:`maxcur` represent the max product ended with A[i-1], when it encounters A[i], it has two choices:absorb A[i] to the product or start a new continuous subarray start with A[i].                 

Time: O(n), Space: O(1)      



