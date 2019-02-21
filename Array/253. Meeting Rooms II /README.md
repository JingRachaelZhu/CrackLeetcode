# 253. Meeting Rooms II  

  

## Ideas  
**idea 1**   
`PriorityQueues` (minheap优先队列)     
Algorithm:    

1.Sort the given meetings by their start time.     
2.Initialize a new min-heap and add the first meeting's ending time to the heap. We simply need to keep track of the ending times as that tells us when a meeting room will get free.      
3.For every meeting room check if the minimum element of the heap i.e. the room at the top of the heap is free or not.     
4.If the room is free, then we extract the topmost element and add it back with the ending time of the current meeting we are processing.
5.If not, then we allocate a new room and add it to the heap.      
6.After processing all the meetings, the size of the heap will tell us the number of rooms allocated. This will be the minimum number of rooms needed to accommodate all the meetings.      
  

**NOTICE**      
* **Understanding the underlying algorithm**: **keep track of the ending times as that tells us when a meeting room will get free.**             
* **Time complexity**:There are two parts.Firstly,Sorting array need O(nlogn),the other part is min heap.Cuz min heap is a binary heap,with O(logn) push and O(logn )pop.The second part is still O(nlgon).So total time is O(nlogn).           
* **Space complexity**:Because we construct the min-heap and that can contain n elements in the worst case as described above in the time complexity section. Hence, the space complexity is O(n).      

Time: O(nlogn), Space: O(n)      


**idea 2**   
`Chronological Ordering` (Smart way)     
Algorithm:     

1.Separate out the start times and the end times in their separate arrays.
2.Sort the start times and the end times separately. Note that this will mess up the original correspondence of start times and end times. They will be treated individually now.
3.We consider two pointers: index_s and index_e which refer to start pointer and end pointer. The start pointer simply iterates over all the meetings and **the end pointer helps us track if a meeting has ended and if we can reuse a room**.
4.When considering a specific meeting pointed to by index_s, we check if this start timing is greater than the meeting pointed to by index_e. If this is the case then that would mean some meeting has ended by the time the meeting at index_s had to start. So we can reuse one of the rooms. Otherwise, we have to allocate a new room.
5.If a meeting has indeed ended i.e. if start[index_s] >= end[index_e], then we increment index_e.
6.Repeat this process until index_s processes all of the meetings.
   
**NOTICE**      
* **Edge case**: when list is None or only have one item,return 0.      
          

Time: O(nlogn), Space: O(n)    

