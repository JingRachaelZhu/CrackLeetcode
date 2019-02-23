# 266. Palindrome Permutation      

**Palindrome condition**: **If the num of odd-count charcters is no more than 1 , it is a Palindrome.**      
## Ideas  
**idea 1**   
`set`     
 Iterate over string, adding current character to set if set doesn't contain that character, or removing current character from set if set contains it.   
 For 2 result which satisfied with palindrome condition:    
1. if len(set1)==0 :corresponds to the situation when there are even number of any character in the string    
2. if len(set1)==1 : corresponsds to the fact that there are even number of any character except one.


**NOTICE**    
* **Should return `pre.next`**:     

Time: O(n), Space: O(n)      

**idea 2**        
`Hashtable`    

The main idea is using hashtable to record the count of character appeared in the string. Then use if statement to judge Palindrome condition.     
`oddcount` : represent for the odd count of characters   
`evencount` : represent for the even count of characters   
**NOTICE**     
* **Palindrome condition**: **If `oddcount` >1, nomatter what `evencount` is ,it is not a Palindrome.** 

Time: O(n), Space: O(n) 
