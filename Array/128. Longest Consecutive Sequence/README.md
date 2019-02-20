# 128. Longest Consecutive Sequence       
  

## Ideas  
**idea 1**   
`set`(no duplicates)     
Using set to remove the duplicaates and remove item(.remove()) in set is O(1),as well as .pop().So **we can search consecutive sequeue both upward and downward and store the lengths with `left` and `right` respectively.** For downward, when going through items in set, check if `value-1` exsits .If so, add `left` by 1 where `left` means the consecutive nums before current value.Then check the `value+2`,until it not in the set.Do the same thing for checking the `value+1`.
   

**NOTICE**      
* **Edge case**: when list is None or only have one value      
* **Delete after visiting **: The value once visited should be removed ,so that it will prevent the repeat searching.Using `while` loop instead of `for` loop ,cuz the size of set will decrease along with visiting items.           
* **Time complexity**:Because it is set, `set.remove()`,`set.pop()` and `in` operation are all **O(1)**. So the total time complexity is O(n).            

Time: O(n), Space: O(1)  

**idea 2**   
`Hashmap` (dict)    
When using dict,key is the items in array,value is the length of the consecutive sequeue which ends with corresponding item. 
**The key thing is to keep track of the sequence length and store that in the boundary points of the sequence.**
Whenever a new element n is inserted into the map, do two things:

See if `i - 1` and `i + 1` exist in the map. If so, it means there is an existing sequence next to i. Variables left and right will be the length of those two sequences, while 0 means there is no sequence and n will be the boundary point later. 
**Use `left` and `right` to locate the other end of the sequences to the left and right of n respectively, and replace the value with the new length.**
   

**NOTICE**      
* **Edge case**: when list is None or only have one value        
* **Time complexity**:Because it is dict, `set.remove()`,`set.pop()` and `in` operation are all **O(1)**. So the total time complexity is O(n).            

Time: O(n), Space: O(n)(the Dictionary class is implemented as a hash table)     



