# 45. Jump Game II       

Your goal is to reach the last index in the minimum number of jumps.        

## Ideas  
**idea 1**     
`BFS with Greedy`         
We can use BFS structure to solve this problem based on Greedy. Use Greedy to define the `furthest` point each point can jump to.Let's say the range of jump is [start,end].traversing all the point on one level,and when current point reaches the boundary of current jump level,jump to the next level. 

**NOTICE**      
* **The main idea**:The key is to find out how many jumps we need instead of the detail track for jump.So think about BFS with levels traversing.
* **the step range**: only need len(nums)-1 point to jump with( `for i in range(len(nums)-1):`) instead of len(nums).    
           

Time: O(n), Space: O(1)      



