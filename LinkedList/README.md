
# Linked list solution in python3  
***
## LINKED LIST
  In order to implement an unordered list, we will construct what is commonly known as a `linked list`.It is important to note that the location of the first item of the list must be explicitly specified. Once we know where the first item is, the first item can tell us where the second is, and so on. The external reference is often referred to as the `head` of the list. Similarly, the last item needs to know that there is no next item.       
## The Node Class  
The basic building block for the linked list implementation is the `node`.Each node object must hold at least two pieces of information. One is the list item itself(`self.data`). The other one is a reference to the next node(`self.next`):    
``` 
lass Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None  
```
## problems：  
1. add,swap and remove(duplicate)     
2. reverse and rotate  
3. merge sorted Linked List
4. Palindrome Linked List 








