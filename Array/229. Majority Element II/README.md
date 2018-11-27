# 229. Majority Element II  
  
## Ideas  
**idea 1**   
`Boyer-Moore Majority Vote algorithm`   
It is a upgrade version of [169.Majority Element](https://github.com/JingRachaelZhu/CrackLeetcode/tree/JingRachaelZhu-patch-1/Array/169.%20Majority%20Element).
Use Boyer-Moore Majority Vote algorithm to solve it.The algorithm uses O(1) extra space and O(N) time. It requires exactly 2 passes over the input list.In the first pass, we generate candidate values if they exist.The second pass simply counts the frequency of that value to confirm.   
In the first pass, we need 2 values:(**Since it should appear more then ⌊ n/3 ⌋ times,the answer should be at most 2 values**)

Two candidate values, initially set to any value(eg. 0,1).
Two count, initially set to 0.
For each element in our input list, we first examine the count value. If the count is equal to 0 , we set the candidate to the value at the current element. Next, first compare the element's value to the current candidate value. If they are the same, we increment count by 1. If they are different, we decrement count by 1. 

**NOTICE**      
* **Two pass**: One is to select possible candidates,the other one is to verify the candidate.      
* **How it works for the first pass**:The range of elements from the time candidate is first assigned to when count drops to 0 can be discarded from the input without affecting the final result of the first pass of the algorithm. We can repeat this over and over again discarding ranges that prefix our input until we find a range that is a suffix of our input where count never drops to 0.     
* **The importance of the second pass**:example:[1,1,1,3,3,2,2],the candidate values are 1 and 2,while 2 is not the correct one we want.Should verify the frenquency of each candidate at last.

Time: O(n), Space: O(1)      



