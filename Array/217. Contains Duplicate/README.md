# 217. Contains Duplicate  

Given an array of integers, find if the array contains any duplicates.    

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

**Example 1:**

Input: [1,2,3,1]   
Output: true 

**Example 2:**   

Input: [1,2,3,4]   
Output: false 

**Example 3:**   

Input: [1,1,1,3,3,4,3,2,4,2]    
Output: true    
   
## Ideas  
**idea 1**   
`set`    
It is quite easy but a good example for time-space tradeoff.Try different way to solve it.  
1.Brute force: T=O(n^2),S =O(1)      
2.Sort: T=O(nlogn),S =O(1)  optimal solution for space       
3.Hashtable:T=O(n),S =O(n)    
4.set :T=O(1),S =O(n) ?      optimal solution for time    

**NOTICE**      
* **Edge case**: when list id None or only have oneor two node,return    
* **After finding mid node(`slow`)**:The `slow.next` will be the beginning of the `sec_half`.`slow` will be the last node of the result,so `slow.next` =`None`.           

Time: O(n), Space: O(1)      



