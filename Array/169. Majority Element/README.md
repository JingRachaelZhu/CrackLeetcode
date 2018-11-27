# 169. Majority Element  

Easy,seldom ask 

## Ideas  
**idea 1**(Sorting)      
Sort the list, if there is a majority value it must now be the middle value. To confirm it's the majority, run another pass through the list and count it's frequency.     

**NOTICE**          
* **Time complexity**:It is O(nlgn) due to the sort though.             

Time: O(nlgn), Space: O(1)     

**idea 2**(hashtable(dict))        
use hashtable to store the count of each item.   

Time: O(n), Space: O(n)(due to the new dict)