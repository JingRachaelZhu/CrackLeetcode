# 134. Gas Station  

**Ideas after observation**:   
* 1.No matter where it starts, if total gas >= total cost,there must be a solution.(After travel around the circuit,the remaining gas in the tank should be >=0)   
* 2.If car starts at A and can not reach B. Any station between A and B can not reach B.(B is the first station that A can not reach.)   

## Ideas  
**idea 1**   
`One pass`
Or use two pass to understand it:        
Use the first pass to determine if we have a solution(property 2 above). Then use the second pass to find out the start positon(use property 1). After you are comfortable with 2 passes, you can absolutely modify it into one pass solution.   

**NOTICE**          
* **`tank`**:It means the current remaining gas in car.When `tank <0`,the car cant reach the `i`th station from where it starts.So the start station should change to `i+1` .   

Time: O(n), Space: O(1)      

**idea 2**   
`start from end`     
The basic idea is every time we start from a station, we go as far as possible by increasing end until remaining gas is less than 0. If 'end' finally hits start we know we can travel around from 'start'. If we haven't traveled around, we know we cannot start from this station. Then we check the station before our start station if we can start from this station. Repeat until we have checked all stations.           

**NOTICE**          
* **Start from the end**: Note there is a little trick that every time we try to find the next start station, we always to back to extend the distance from start to end so that we can check all stations on the circuit. Otherwise, if we move start forward to decrease the distance from start to end, we are likely to end up with only checking part of the circuit. Another trick is we start from the end of the array so as to avoid some corner cases.          

Time: O(n), Space: O(1) 

