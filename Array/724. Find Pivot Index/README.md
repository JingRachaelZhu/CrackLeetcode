# 724. Find Pivot Index  
  
## Ideas  
**idea 1**   
`iteration`    
While iterating the whole array,keep track of the sum of the values on the current number's left and its right.Initialize `right` to `sum(nums)` and `left` to `0`.    

**NOTICE**      
* **Understand correctly**:It means **the sum of nums** on each side(not include the pivot num), not the nums of nums on each side!!!     
* **The position of the addition of `left`**:should put it after comparing the equivalence of `right` and `left`.It is be added the current num for next .   

Time: O(n), Space: O(1)      



