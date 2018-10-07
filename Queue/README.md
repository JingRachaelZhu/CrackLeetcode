# Queue solution in python 3  
***
## QUEUE
  A queue is an ordered collection of items where the addition of new items happens at one end, called the “rear,” and the removal of existing items occurs at the other end, commonly called the “front.” As an element enters the queue it starts at the rear and makes its way toward the front, waiting until that time when it is the next element to be removed.    
**Order: FIFO (first in,first out 先进先出)**    
## Abstract Data Type  
* `Queue()` creates a new queue that is empty. It needs no parameters and returns an empty queue.  
* `enqueue(item)` adds a new item to the rear of the queue. It needs the item and returns nothing.  
* `dequeue()` removes the front item from the queue. It needs no parameters and returns the item. The queue is modified.  
* `isEmpty()` tests to see whether the queue is empty. It needs no parameters and returns a boolean value.  
* `size()` returns the number of items in the queue. It needs no parameters and returns an integer.     
   
We need to decide which end of the list to use as the rear and which to use as the front. The implementation assumes that the rear is at position 0 in the list. This allows us to use the insert function on lists to add new elements to the rear of the queue.(O(n)) The pop operation can be used to remove the front element (the last element of the list).(O(1)):
``` 
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)  
```
## problems：    
1. Tree的Breadth search（BFS) 
