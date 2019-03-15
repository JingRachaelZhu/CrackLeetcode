# 162. Find Peak Element                     

## Ideas  
**idea 1**   
`Binary Search`(iterative)        
It need find the peek item ,which is greater than its neighbors.The key condition is to compare two adjacent items.Finally, left =right point to the peek item         


**NOTICE**         
* **If nums[mid] < nums[mid+1]**: `left = mid +1`Because `mid+1` could be the peek item index.If not, `right =mid`,right could be the peek item index.          
* **Edge case**: when len(nums) ==1,return 0.                     

Time: O(logn), Space: O(1)   

**idea 2**   
`Binary Search`(recursion)        
We can also solve it in a recurision way.Bulid a helper funtion to do the binary search.           
              

Time: O(logn), Space: O(logn) reduce the search space in half at every step. Thus, the total search space will be consumed in log_2(n) steps. Thus, the depth of recursion tree will go upto log_2(n).      





