# 11. Container With Most Water       
 

## Ideas  
**idea 1**   
`Two Pointers`   
To get the most water in the container, we should figure out the factors when calculating the area of the container. That is the width and the height .Compared with the width,the height is the main factor in this problem.What's more, the smaller one between left and right line determines the height of the container.So we need to change the height (especially the smaller line) to get max area.    


**NOTICE**         
* **understanding it throughly**: The small line is the key factor of area calculation.              

Time: O(n), Space: O(1)      



