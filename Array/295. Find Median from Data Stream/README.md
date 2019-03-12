# 220. Contains Duplicate III       

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.     

For example,    
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5     

Design a data structure that supports the following two operations:           

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.    
          

## Ideas  
**idea 1**   
`PriorityQueue`(heap)      
It is a `Design` problem to find the median num in a list.**The fact that we only need a consistent way to access the median elements. Keeping the entire input sorted (sort technology)is not a requirement.**        
If we could maintain two heaps in the following way:     

A max-heap to store the smaller half of the input numbers     
A min-heap to store the larger half of the input numbers          
                  

**NOTICE**      
* **Find the resonable data structure**:The key is we only need access the median nums instead of keeping the whole list sorted.      
* **The maxheap for smaller helf**:Since we need the largest one on the top of this hea, we can take the opposite number of each nums while pushing into the heap.                 

Time: O(logn),`push` and `pop` take O(logn) i heap.Finding the mean takes constant O(1) time since the tops of heaps are directly accessible.      
Space: O(n) (linear space to hold input in containers.)                     
