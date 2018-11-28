# 275. H-Index II    

Follow up:

This is a follow up problem to [274.H-Index](https://github.com/JingRachaelZhu/CrackLeetcode/tree/JingRachaelZhu-patch-1/Array/274.%20H-Index), where citations is now guaranteed to be sorted in ascending order.
Could you solve it in logarithmic time complexity?       

## Ideas  
**idea 1**   
`binary search`     
case 1: citations[mid] == len-mid, then it means there are citations[mid] papers that have at least citations[mid] citations.
case 2: citations[mid] > len-mid, then it means there are citations[mid] papers that have moret than citations[mid] citations, so we should continue searching in the left half
case 3: citations[mid] < len-mid, we should continue searching in the right side
After iteration, it is guaranteed that `right+1` is the one we need to find (i.e. `len-(right+1)` papars have at least `len-(righ+1)` citations)      
**NOTICE**      
* **be sorted in ascending order**: need to use binary search to find the result    
 * **if citations[mid] == length-mid:return length-mid**:It means 'length-mid' of all papers have at least 'citations[mid]' citations each     
* **Final return**:If it doesn't hit the condition `citations[mid]== (len-mid)`,finally `right` will be on the left of `left`.And the `right+1` wil be the target num we need.so the result is `length-(right+1)`.eg.[0,1,3,4]            

Time: O(logn), Space: O(1)      



