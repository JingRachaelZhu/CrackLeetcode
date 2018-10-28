# 27. Remove Element      

Given an array nums and a value val, remove all instances of that value in-place and return the new length.  

Do not allocate extra space for another array, you must do this by modifying the input array **in-place with O(1) extra memory**.  

**The order of elements can be changed. It doesn't matter what you leave beyond the new length.**  

**Example 1:**  

Given nums = [3,2,2,3], val = 3,  

Your function should return length = 2, with the first two elements of nums being 2.  

It doesn't matter what you leave beyond the returned length.   

**Example 2:**  

Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.      

## Ideas  
**idea 1**(reassign)    
Since It doesn't matter what you leave beyond the returned length,it's OK to reassign the value of the list from beginning . while iterating the whole list,if the vale of the item is not equal to `val`,then assign this value to `num[ct]`（`ct` starts from 0）      

**NOTICE**      
* **in place algorithm(O(1))**:`.remove()`is O(n) funtion ,if it is inside a for loop , the overall time complexity will be O(n^2).So don't do that way.  
* **Read topic description carefully**:It only requests to return the num of target items and **The order of elements can be changed. It doesn't matter what you leave beyond the new length.** It tends to ask me to **manipulate the list (swapping or reassigning values)** instead of getting rid of partial values (removing or deleting values).   
          
Time: O(n), Space: O(1)  

 **idea 2**(swap)   
Similar to `idea 1` ,it has more integrality for swapping the two items from both side of the list. when two nodes meet, the whole search is over.   
**NOTICE**        
* **Terminal condition**:when the `left` is equal to `right`, it still need to be judged if the value of the item is equal to `val`. So the terminal condition is `left <= right`.  

Time: O(n), Space: O(1) 


