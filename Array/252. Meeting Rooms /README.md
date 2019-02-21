# 164. Maximum Gap 

  

## Ideas  
**idea 1**   
`Bucket sort` (linear time )    
 
 

**NOTICE**      
* **Edge case**: when list is None or only have one item,return 0.      
        

Time: O(n), Space: O(1)      


**idea 2**   
`sort` (nlogn time )     
keep track of the diff of each pair items in the sorted array and store the max diff into result.   
   
**NOTICE**      
* **Edge case**: when list is None or only have one item,return 0.      
          

Time: O(nlogn), Space: O(1) 

