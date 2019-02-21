# 53. Maximum Subarray         

## Ideas  
**idea 1**   
`Kadane's algorithm`卡登算法      
    
`Kadane's algorithm`:      
In simple terms, it states that, the maximum sum sub-array ending with A[i], is either the element A[i] itself, or A[i] combined with the maximum sum sub-array ending with A[i – 1], whichever is the greater one.  
     

**NOTICE**      
* **Edge case**: when list is None ,return .     
* **Understanding Kadane's algorithm**:the maximum sum sub-array ending with A[i], is either the element A[i] itself, or A[i] combined with the maximum sum sub-array ending with A[i – 1].         

Time: O(n), Space: O(1)  
