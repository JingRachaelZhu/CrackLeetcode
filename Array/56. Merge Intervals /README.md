# 56. Merge Intervals         

## Ideas  
**idea 1**              
`sort`(Intervals)   
 t is similiar to 252. Meeting Rooms,but a update version.The idea is to **sort the intervals by their starting points**. Then,go through the intervals sorted by start coordinate and either combine the current interval with the previous one if they overlap, or add it to the output by itself if they don't.

**NOTICE**          
* **Sorted the list by starting point**:Use lambda funtion to define i ,then get i.start.     
 * **When extend the `res`**: use `res +=[i]`.Even though i is a list,if use `res +=i`,the result will be[1,2,3,4].no [] in btween.

Time: O(nlogn)(sorted), Space: O(1)(no extrs space)        
 
  


