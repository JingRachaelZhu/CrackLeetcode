# 3. Longest Substring Without Repeating Characters                                    

## Ideas  
**idea 1**   
`Hashtable with two pointers`        
the basic idea is, keep a hashmap which stores the characters and their positions, and keep two pointers which define the max substring. move the right pointer to scan through the string, and meanwhile update the hashmap. If the character is already in the hashmap, then move the left pointer to the right of the same character last found. **Note that the two pointers can only move forward**(eg. 'abba').         


**NOTICE**         
* **When encountering the repeat char**:update the `maxlen`,`start` point and the location(char[s[i]]) of repeat char stored in the dict.Be carefully when we updating the start point, it could not move backward,which means start should be max(start,char[s[i]]+1).                     

Time: O(n), Space: O(n)             



