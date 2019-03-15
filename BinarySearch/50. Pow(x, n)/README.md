# 50. Pow(x, n)     
Implement pow(x, n), which calculates x raised to the power n (xn).                       

## Ideas  
**idea 1**   
`Binary Search`        
 Brute Force solution is very straightforward ,which has the time complexity O(n).In order to improve it ,we can use binary search ,which has O(logn) time complexity.**Key:convert the n to binary representation.eg. 2^6 =2^110 =(2^4) * (2^2)**.           


**NOTICE**         
* **Convert into binary representation**: Like the mod operation ,make it clear which is **each value for next digit**.                 
                     

Time: O(logn), Space: O(1)   
     





