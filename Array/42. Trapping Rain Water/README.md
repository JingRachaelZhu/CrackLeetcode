# 42. Trapping Rain Water

update version of 11. Container With Most Water  

## Ideas  
**idea 1**   
`two pointers`     
In order to hole water ,we need 2 barriers and 1 smaller retangle in the middle .Solve it in a cumulative way. Keep track of the maximum height from both forward directions backward directions and the diff between shorter retangle and the crosponding `maxleft/maxright` is the subsum of water. 
  

**NOTICE**      
* **simplify the problem**:devide it into subpart to analyse.     
* **Do we need the `=` in while statment?**: No. When left ==right,there is only 2 line left ,which can't hold water any more.No subsum need to be added to final result.        

Time: O(n), Space: O(1)      



