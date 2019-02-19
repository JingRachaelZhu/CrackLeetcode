# 121. Best Time to Buy and Sell Stock     

## Ideas  
**idea 1**   
`Kadane's algorithm`卡登算法    
**It is similar to `53. Maximum Subarray`. We need to find out the largest sum subarray to get the most profit.** 
eg.To find most profit in {7,1,5,3,6,4} is the same as to find the largest sum subarray in {0,-6,4,-2,3,-2} the value is the diff of two contiguous values in former array.      
     

**NOTICE**      
* **Edge case**: when list is None or only have one node,return 0.     
* **When applying Kadane's algorithm**:The orignal max_ending_here in K algorithm is `max_ending_here = max(0,max_ending_here + a[i])`.When applying in this secific case, it should be `max_ending_here = max(0,max_ending_here + prices[i]-prices[i-1])`.The difference of two contiguous values is the value that max_ending_here needs to add.      

Time: O(n), Space: O(1)   


**idea 2**   
`iteration`       
It looks for the smallest value among the array and keep track of the larget profit by comparing former most profit and current profit.     
      

**NOTICE**      
* **Edge case**: when list is None or only have one node,return 0.     
      

Time: O(n), Space: O(1) 


