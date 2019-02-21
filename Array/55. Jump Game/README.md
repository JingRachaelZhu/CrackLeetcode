56. Merge Intervals# 55. Jump Game     

## Ideas  
**idea 1**(move forward)         
`Greedy`   
It can be solved by Greedy.At each step,move forward and update the `furthest` position.If the `furthest` is in the front of current index(`furthest < i`),which means we can't reach current index,return `False`. 

**NOTICE**          
* **Greedy thinking**: making the locally optimal choice at each stage with the intent of finding a global optimum.      

Time: O(n)(one pass), Space: O(1)(no extrs space)        



**idea 2**(move backward)    
`Greedy`   
It can be solved by Greedy.At each step,move forward and update the `furthest` position.If the `furthest` is in the front of current index(`furthest < i`),which means we can't reach current index,return `False`.      

Time: O(n)(one pass), Space: O(1)(no extrs space)         


idea 3 :DP  
  


