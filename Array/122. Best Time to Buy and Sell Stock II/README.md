# 122. Best Time to Buy and Sell Stock II      
   

## Ideas  
**idea 1**   
`Greedy` (pairwise diff)     
since 100-0 =(50-0)+(100-50), so we can solve it by Greedy. find the opsitive diff and caculate the total sum of opsitive diff to get the most profit.     
   
**NOTICE**      
* **Edge case**: when list is None or only have one node,return 0.              

Time: O(n), Space: O(1)      



