# 119. Pascal's Triangle  II  

Easy,seldom ask 

## Ideas  
**idea 1**   
Find the rule .The trick here is to find the pattern that **each row's [i]th index is actually the sum of [i] and [i-1] of the previous row**. Note: each row will increase by 1 number length, that new element defaults to 0, those values are bold in the above example.   

**NOTICE**          
* **Initialization**:initialize the list to [0,0,0...] ,every element is defaults to 0 (`res =[0]*(rowIndex+1)`)            

Time: O(n^2), Space: O(n) 

**idea 2**(Pythonic way)        
use map or zip to caculate the items of each row.Initialize `res`to [1]   

**NOTICE**           
* **Understanding**: The rule is the same as `idea 1`.For example, if `rowIndex` is 1, [0,1]represents the item ahead the current position of previous row, [1,0] represents the item on current position of previous row.Then follow the rule:**row[i][j] =row[i-1][j-1] +row[i-1][j]** It will come to [1,1],which is the 1th row.       

Time: O(n^2), Space: O(n)