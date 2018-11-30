# 245. Shortest Word Distance III      

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.     

**word1 and word2 may be the same and they represent two individual words in the list.**     

**Example:**
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].    

Input: word1 = “makes”, word2 = “coding”    
Output: 1    
Input: word1 = "makes", word2 = "makes"    
Output: 3    

**Note:**
You may assume word1 and word2 are both in the list.      

## Ideas  
**idea 1**   
`One pointer` (similar to `243.idead 2`)   
It is the samee idea to `idea 2` of [243. Shortest Word Distance ](https://github.com/JingRachaelZhu/CrackLeetcode/tree/JingRachaelZhu-patch-1/Array/243.%20Shortest%20Word%20Distance)    

**NOTICE**      
* **two situations**: Whether this two word are equal or not, use the same idea to solve:The varialbe `a` tracks the position of two words and former `a` represents the position of one word while current `i` represents the another one's position.So `dis =min(dis,i-a)`.                        

Time: O(n), Space: O(1)      



