# 274. H-Index    

## Ideas  
**idea 1**(optimal)   
`bucket sort`      
 the h-index is defined as the number of papers with reference greater than the number. So assume `n` is the total number of papers, if we have `n+1` buckets, number from `0` to `n`, then for any paper with reference corresponding to the index of the bucket, we increment the count for that bucket. The only exception is that for any paper with larger number of reference than n, we put in the `n-th` bucket.    

 Then we iterate from the back to the front of the buckets(since finding the maximum one as the h-index), whenever the total count exceeds or equal to the index of the bucket, meaning that we have the index number of papers that have reference greater than or equal to the index. Which will be our h-index result.   

**NOTICE**      
* **convert realworld problem into a algorithm problem**: The key point of this problem : consider different kind of examples and conclude it as a algorithm problem to solve.     
          

Time: O(n), Space: O(n)     

 **idea 2**   
`sort`     
sorting the input list in place.Then if the value(`citations[i]`) is equal to or greater than the nums of the values behind it in the list(`length-i`),meaning the `length-i` of N papers has at least `citations[i]` citations each, which is the result answer. 
   
**NOTICE**      
* **convert realworld problem into a algorithm problem**: The key point of this problem : consider different kind of examples and conclude it as a algorithm problem to solve.               

Time: O(nlgn), Space: O(n)   



