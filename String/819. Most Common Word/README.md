# 819. Most Common Word                  
 

## Ideas  
**idea**   
`hashtable`        
The problem need to return the most frequent word appeared in the string. Using a hashtable to record the count of each word. When the word is in the banned list,just ignore it and process to next word.    


**NOTICE**         
* **Deal with the string**: First,we need to replace the punctuation symbols with whitespace.And convert string to a list of string.Another way is to use Regular expression:`str1 =re.findall(r"\w+", str1)`         
* **If the result has more than one word**: To handle this problem,we use a list to store the most frequent words.And finnally convert the list into string.`''.join(res)`        

Time: O(n+b), Space: O(n+b),where n is the size of string and b is the size of banned list.   



