# 244. Shortest Word Distance II     

Design a class which receives a list of words in the **constructor**, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list. Your method will be called repeatedly many times with different parameters.    

**Example:**   
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].   

Input: word1 = “coding”, word2 = “practice”   
Output: 3   
Input: word1 = "makes", word2 = "coding"   
Output: 1    

**Note:**
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.         

## Ideas  
**idea 1**   
`Design`(hashmap)   
1.When it comes to constructor,recall :dictionary(hashtable/hashmap),list,tuple and set.Use dictionary(hashmap) for this problem.    
2.Get the values of two lists from word1 and word2,and generate the minmum value of `dis`.It continues until either one list is exhausted.      

**NOTICE**      
* **defaultdict**:Don't forget to add `from collections import defaultdict`statement .**defaultdict(list) is used to group a sequence of key-value pairs into a dictionary of lists.**defaultdict(int) is used for counting.     
* **When generating dis**:The terminal condition for while loop is either one list is exhausted(use `and` ).Compare two value to decide which list next value is from.                

Time: O(n), Space: O(1)      



