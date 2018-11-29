# 243. Shortest Word Distance 

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.          

**Example 1:**    

Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3    

Input: word1 = “coding”, word2 = “practice”
Output: 3    

**Note:**
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.       

## Ideas  
**idea 1**   
`Two pointer`    
It use two pointers `a`,`b` to track the position of each word,respectively.Once find both two words,assign the minimun vaue between `dis` and `a-b`(or `b-a`) to `dis` .  

**NOTICE**      
* **initialize `dis`, `a`and`b`**: No need to initialize `dis` to infinity(`float("inf")`),dis is no greater than the length of the list(`len(words)`).`a` and `b` both set to `-1` or `None`,which are not in the range of index.         
* **While update `dis`**:Without putting `dis` assigment statement in the buttom of for loop,put it in each `if` statement to prevent using `abs` funtion.                 
Time: O(n), Space: O(1)      

**idea 2**   
`One pointer`    
It use one pointer `index` to track the position of both words.similiar to `idea 1`.         

**NOTICE**               
* **While update `dis`**:unlike `idea 1`,when finding possible index,need to check it to make sure that 1. found a word before(`index !=-1`) 2.the former found word is not the same as the current found word(`words[index]!=words[i]`).                  
Time: O(n), Space: O(1)

