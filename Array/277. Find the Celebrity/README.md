# 277. Find the Celebrity    

Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. **The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.**  

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).  

You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n), your function should minimize the number of calls to knows.  

Note: There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.      

## Ideas  
**idea 1**(Brute force)    
`iteration`   
It does as the topic described. First,initilize every item of a new array `res`(length is `n`) to `True` ,which keep track of the state of every person,assuming candidate in order from `0` to `n-1`.When selected `i` as candidate,iterating all other people`j`,calling funtion `knows(i,j)`to see if i kns j.If not celebrity,set its related value to `False`.Finally,return its label if have a celebrity. 

**NOTICE**      
* **Edge case**: when `n` is None ,return `-1`     
* **Each time calling funtion knows(i,j)**: `i` should compare with other all people except itself.If `i` kn `j`,`i` can't be the celebriity,if `i` doesn't kn `j`,`j` can't be the celebrity.So each time after calling `knows(i,j)`,should discard one person.      

Time: O(n^2)(nested loop), Space: O(n)(new array) 

**Improved solution**   
**use key1:celebrity kns noone** to select a candidate. It doesn't need a new array but a mark `cel`to keep track of the funtion `knows()` result.Just to mark`cel` `False` if `knows(i,j)` is `True` and turn to next person.Finally,if `cel` is `True`after iterating all other people,means the candidate kns noone.  
Then use **key2:everyone kns celebrity** to check if all others knows this candidate.   

Time: O(n^2)(nested loop), Space: O(1)(constant space)

**idea 2**(Queue , Stack)     
`iteration`    
Creating a queue to store all labels. When iterating the `Queue`,each time calling funtion `knows(A,B)` and add the candidate to the tail of the queue--**O(n)** for later comparison.When the length of the queue is 1, selecting candidate is over.Finally,check the candidate if it satisfies both two conditions.   

**NOTICE**      
* **Queue tail and head**: it depends.could be the head(array) as head--pop(0) and the tail(array) as tail--append(item) .Or the tail(array) as head--pop() and the head(array) as tail--insert(0,item).Both of two ways have the same time complexity:one is O(n),one is O(1).             
* **Check the candidate**:Since first step just compares two persons each time, it's necessary to check the candidate at last.  

Time: O(n^2), Space: O(1) 

**improved solution**(Stack,similar to Queue solution,but more faster(push&pop both O(1))          
It's similiar to `Queue solution`.The difference is after first time pop two persons , just pop one person per time to compare with former candidate.When the stack is empty, need to call knows(i,j) to find the final candidate.Finally,check the candidate as well.  

**NOTICE**      
* **compare Time complexity with Queue**: Stack is faster.Since the two step push&pop both need O(1),so the total time complexity is O(n) while Queue needs O(n^2).               
* **Check the candidate**:Since first step just compares two persons each time, it's necessary to check thecandidate at last.  


Time: O(n), Space: O(1)

**idea 3**(more elegant solution,no stack or queue)**final optimal solution**     
`iteration`    
The Key is every time after calling funtion `knows(i,j)`,it can descard one person.So Once find `i` kns `j`,set `j` as candidate and compare `j` with latter people.At last ,check the candidate.  

**NOTICE**        
* **Optimize checking step**: When checking the candidate, need to check 2 conditions:One is all other persons kn candidate .The other one is the candidate does not kn anyone.For the latter condition,the first step has already checked out the candidate does not kn people behind him/her.So just need to check if the candidate kns people ahead of him/her.(`i <candidate and knows(candidate,i)`)        
           
Time: O(n), Space: O(1)
