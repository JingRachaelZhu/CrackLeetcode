# 209. Minimum Size Subarray Sum                              
 

## Ideas  
**idea 1**   
`Two pointers`        
It can be solved by using two pointers.One is the `start` point,the other is the `end` point of substring.When interating the array, use while loop to keep adjust the `maxcur` and the s`tart` point of the substring. 


**NOTICE**         
* **Edge case**: if the array is `None` or `[]`,return 0.If the sum of all items in array is less than `s`,return 0.                    
* **How to control the `sumcur` and the `start` point move**: Using while loop to adjust the `maxcur` and move forward the start point.          

Time: O(n), Space: O(1)         

**idea 2**   
`Binary search`        
It can also be solved by using  binary search when comes to find the start point.First, get every accumulative sum on each postion.When the accumulative sum is greater than `target`, find the start point using binary search.          


**NOTICE**         
* **Edge case**: if the array is `None` or `[]`,return 0.If the sum of all items in array is less than `s`,return 0.                    
* **First,accumulative sum,then find start point**:          

Time: O(nlogn), Space: O(1) ,since binary search is O(logn).        



