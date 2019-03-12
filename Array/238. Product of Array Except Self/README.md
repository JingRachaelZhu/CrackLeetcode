# 238. Product of Array Except Self        

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].      
Note: Please solve it without division and in O(n).               

## Ideas  
**idea**   
`iteration`    
It can divide multiplication into two parts to complete the whole division.First, multiply the nums in front of current num to get the `leftside product`.Secondly, multipy the nums  behind the current num to get the `rightside product`. 

**NOTICE**      
* **Divide multiplication into two parts**:Multiply the nums on the leftside and rightside respectively.         
* **Initialize left/right value**:Cuz we need num multiply by `left/right`. So it should be initilize to be 1.                    

Time: O(n), Space: O(1)      



