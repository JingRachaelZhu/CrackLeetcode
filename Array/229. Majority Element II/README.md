# 229. Majority Element II  
  
## Ideas  
**idea 1**   
`Boyer-Moore Majority Vote algorithm`   
   
  

**NOTICE**      
* **Edge case**: when list id None or only have oneor two node,return    
* **After finding mid node(`slow`)**:The `slow.next` will be the beginning of the `sec_half`.`slow` will be the last node of the result,so `slow.next` =`None`.           

Time: O(n), Space: O(1)      



