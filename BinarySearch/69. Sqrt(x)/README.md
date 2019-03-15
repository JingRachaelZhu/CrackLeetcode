# 69. Sqrt(x)             
 

## Ideas  
**idea**   
`Binary Search`   
It has two part ascending order.So if we can find which part the target is in ,then apply binary search to find the target.First, find the one ascending order part:  `if nums[left] <= nums[mid]`
Then check if the target is in the ascending order part:`if nums[left] <=target <=nums[mid]`.Use binary search to shrink the range.           


**NOTICE**         
* **Main idea**: Find the two parts ,then search in the certain ascending order part.Use binary search to shrink the range.                     

Time: O(logn), Space: O(1)      



