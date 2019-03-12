# 929. Unique Email Addresses             
 

## Ideas  
**idea**   
`hashset`(Split funtion)   
It canbe solved by using `split.()` funtion to normalize the email address ,then add it to `set` .Since `set` has no duplicate,the length of `set` is exactly the nums of unique email addresses.    


**NOTICE**         
* **use set to remove duplicate**: The small line is the key factor of area calculation.              

Time: O(n), Space: O(n),where n is the content of `emails` list.   



