# 334. Increasing Triplet Subsequence


## Ideas  
**idea 1**   
`iteration` (small,middle,big)   
set small and middle num as MAX value,and compare each value in `nums` to find if there exists 3 values matching the description.

**NOTICE**      
* **Think it loud**: simple comparision. no data structure need
* **Edge case**: when array is None or only have two values,return False        
      

Time: O(n), Space: O(1)      



