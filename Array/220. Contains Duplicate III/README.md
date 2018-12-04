# 220. Contains Duplicate III       

Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.
    
**Example 1:**

Input: nums = [1,2,3,1], k = 3, t = 0     
Output: true      

**Example 2:**

Input: nums = [1,0,1,1], k = 1, t = 2    
Output: true    

**Example 3:**     
 
Input: nums = [1,5,9,1,5,9], k = 2, t = 3    
Output: false        

## Ideas  
**idea 1**   
`bucket sort` (similiar to sliding window)   
It is a upgrade version to [219. Contains Duplicate II ](https://github.com/JingRachaelZhu/CrackLeetcode/tree/JingRachaelZhu-patch-1/Array/219.%20Contains%20Duplicate%20II) ,which changes both the distance(`k`) and value difference(`t`) at the same time. Each bucket has size of `t+1`(in case t ==0). For each number, the possible candidate can only be in the same bucket or the adjacent buckets .And keep as many as `k` buckets to ensure that the difference is at most k.  

**NOTICE**      
* **Understanding the problem well**:It changes two factors at the same time,which means select the two candidates in a certain range with certain value difference.So use bucket sort to solve it.  
* **The range of each bucket and num of bucket**:The range of each bucket should be `t+1`,which prevent the bucket mapping `n =nums[i]//(t+1)` invalid when`t ==0`.The nums of bucket is at most k,since the most distance is k.           

Time: O(n), Space: O(n)(**standard bucket sort:need  `m` buckets extra space and `n` items extra space S(n)=O(n+m)**)      



