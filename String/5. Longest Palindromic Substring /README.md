# 5. Longest Palindromic Substring回文                       
 

## Ideas  
**idea**   
`Dynamic Programming` (Expand Around Center)       
Beacuse of the feature of palindrome, we could use a helper funtion `expandFromCenter` to compare each pair of words.   


**NOTICE**         
* **Understanding the problem**: First,we need to replace the punctuation symbols with whitespace.And convert string to a list of string.Another way is to use Regular expression:`str1 =re.findall(r"\w+", str1)`         
* **If the result has more than one word**: To handle this problem,we use a list to store the most frequent words.And finnally convert the list into string.`''.join(res)`        

Time: O(n^2), Space: O(1),since `expand from center funtion could take O(n)`,so overvall complexity is O(n^2).   



