# 33. Search in Rotated Sorted Array                    
 

## Ideas  
**idea**   
`Binary Search`   
It need return the square root of x and only the integer part of the result is returned.Due to the square operation,we can use binary seach to solve it.The range could be [1,x].    


**NOTICE**         
* **Prevent integer overflow**: Firstly, the `mid` should be `left + (right - left)/2`instead of `(left +right)/2`. Secondly,to prevent `overflow`the integer if `mid` is large enough,we need to use `mid > x/mid` instead of `mid*mid > x`. 
* **Edge case**: when x ==0,return 0.              

Time: O(logn), Space: O(1)      



