# 102. Binary Tree Level Order Traversal                                     
 

## Ideas  
**idea 1**   
`BFS`(queue,iteration)             
It can be solved by BFS with queue.The key point is keep one level items in one list,so we need record the level size for each level. 


**NOTICE**         
* **Edge case**: if root is None or [],return [].                           
* **How to keep level order**: keep track of the level size for each level and iterating the current queue with popping the items of current level and pushing the items of next level.               

Time: O(n),since each node is processed exactly once      
 Space: O(n) to keep the output structure which contains N node values.              

**idea 2**   
`DFS` (recursion)       
It can also be solved by using  binary search when comes to find the start point.First, get every accumulative sum on each postion.When the accumulative sum is greater than `target`, find the start point using binary search.          


**NOTICE**         
* **Edge case**: if the array is `None` or `[]`,return 0.If the sum of all items in array is less than `s`,return 0.                    
* **First,accumulative sum,then find start point**:          

Time: O(nlogn), Space: O(1) ,since binary search is O(logn).        



