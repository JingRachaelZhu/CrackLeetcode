# 1. Two Sum            
 

## Ideas  
**idea 1**   
`brute force` (nested for loop)        
The brute force approach is simple. Loop through each element xx and find if there is another value that equals to target - x.                      

Time: O(n^2), Space: O(1)     

**idea 2**   
`hashtable`                     
 If the complement exists, we need to look up its index. When it comes to a mapping of each element in the array to its index, I think hash table would be a nice way to try.   

Time: O(n), Space: O(n)    

**idea 3**   
`sort + two pointer` （used for 3sum/4sum）                 
 If we wanna optimize  space complexity, we can first sort the array and use two pointers to find the solution.(left and right )Because we still need the orginal index ,so first we could use enumerate to create a counter for the array.(0,2),(1,7),(2,11),(3,15)

Time: O(nlogn), Space: O(1)    


