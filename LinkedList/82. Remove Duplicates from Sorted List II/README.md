# 24. Swap Nodes in Pairs  
vGiven a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.  

**Example 1:**    

Input: 1->2->3->3->4->4->5
Output: 1->2->5  

**Example 2**  

Input: 1->1->1->2->3
Output: 2->3

## Ideas  
**idea 1**   
`iteration`  
To use two vals to track the duplicate and form new list   
1. First,set `dummy` ahead of the `head`of list(cuz there is a case when the `head` is the duplicate).`pre`equals to `dummy`,`cur` equals to `head`     
2. Then track the duplicate ,`cur` will reach to the last node of duplicates. 
3. If the `cur` is next to `pre`,means the current node `cur` has no duplicate,so `pre` reaches to next node(which is `cur`).If not,assign `cur.next` to `pre.next`  
4. After all,cur reaches to next node of the list

**NOTICE**    
* **If loop execute statement**: if `cur` is next to `pre`,means no duplicate currently,take next step(`pre` reaches to next node)      
* **If loop execute statement**: if `cur` is not next to `pre`,means `cur` is duplicate,so assign `cur.next` to `pre.next`.**Attention:** the current `pre.next` may not be the final result.May change to another node in the next loop  

Time: O(n), Space: O(1)      

**idea 2** (Less efficient than idea 1,cuz need more memory and time )   
`iteration` with mark 
1. The only diff with `idea 1` is to add a mark `isDuplicate` for checking duplicate without estimating the location relationship between `cur` and `pre`  

Time: O(n), Space: O(1) 
