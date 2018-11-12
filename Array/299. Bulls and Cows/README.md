# 299. Bulls and Cows     

You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. 

Please note that both secret number and friend's guess may contain duplicate digits.       

**Example 1:**   

Input: secret = "1807", guess = "7810"  

Output: "1A3B"  

Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.    

**Example 2:**  

Input: secret = "1123", guess = "0111"   

Output: "1A1B"  

Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.   

**Note**: You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.      

## Ideas  
**idea 1**      
`two pass`    
First pass for `bulls`: If the items match while iterating two strings,`bulls` add 1 .   
Second pass for  `cows`: create two lists to count the num of each chars appears in `secret` and `guess`,respectively.Then, cows will be added by the smaller num of the given nums in both lists.   

**NOTICE**      
   
* **When counting**:The counts do not include the bulls num so it is inside the `else` part.
* **How to caculate cows?**:Key:the smaller num of counts is the target num.Think about it in realwold problem.     
* **return format**: return string.Python has a printf()-like facility to put together a string.The `%` operator takes a printf-type format string on the left (**`%d` int, `%s` string, `%f`/`%g` floating point**), and the matching values in a tuple on the right,eg:'%dA%sB' % (3,str(3))     

Time: O(n), Space: O(1)(independent with n)   

**idea 2**(optimal solution of `idea 1`)      
`one pass`     
The main diff is the `else` part.It use only one array to record counts from both `secret` and `guess` while `idea 1` uses two array to store counts independently.`Cows` adds 1 when num from `secret` was already seen in `guess` or vice versa.      

**NOTICE**      
   
* **remenber to change type**:The type of `secret[i]` is `str`. So invert `str` into `int`when using`count[secret[i]]`.           
* **How to caculate cows?**:Key:Increment `cows` when either number from `secret` was already seen in `guest` or vice versa.              

Time: O(n), Space: O(1)(independent with n)        



