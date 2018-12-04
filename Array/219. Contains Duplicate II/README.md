# 219. Contains Duplicate II        

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.    

**Example 1:**

Input: nums = [1,2,3,1], k = 3    
Output: true       

**Example 2:**

Input: nums = [1,0,1,1], k = 1    
Output: true   

**Example 3:**

Input: nums = [1,2,3,1,2,3], k = 2    
Output: false       

## Ideas      
**idea 1**   
`sliding window`(set)          
Create a set  and keep the length of set to k+1(sliding window size).Then when adding each latter item in the list,the first item in set will be deleted to mantain the constant window size.Check if the current item is in set,if so ,which means two same items have at most k distance.(`the absolute difference between i and j is at most k`)       

**NOTICE**      
* **Use set is enough**:No need for list.Since the problem only need to testify the existence of that condition,so 1 or 2 same items in windows doesn't matter.             

Time: O(n), Space: O(1)      

**idea 2**   
`hashtable`(pythonic)     
Create a dict and while putting items in it ,check if each two adjacent indices meet the condition(`the absolute difference between i and j is at most k`)    
   

**NOTICE**      
* **Convert condition into logical one**:  `find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k` ,it means the shortest `dis` between two same values(adjacent indices) should not greater than`k`:`if n in dic1 and i-dic1[n] <=k`.         
* **Think outside the box**:Don't create dict and put all items in it without thinking.            

Time: O(n), Space: O(n) 


