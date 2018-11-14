# 118. Pascal's Triangle    

Easy,seldom ask 

## Ideas  
**idea**   
Find the rule .The trick here is to initialize all 1 in each list.(`res =[[1]*(i+1) for i in range(numRows)]`)   

**NOTICE**      
* **Edge case**: when `numRows` is 0 ,return []      
* **the * operation in list**: The * operator produces `a new list` which `"repeats"` the original list's contents.It can only repeat a list in combination with an integer,eg.`the_list * an_integer`.           

Time: O(n^2), Space: O(n)      



