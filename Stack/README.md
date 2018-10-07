# Stack solution in python 3
***
## STACK
  A stack (sometimes called a “push-down stack”) is an ordered collection of items where the addition of new items and the removal of existing items always takes place at the same end. Stacks are fundamentally important, as they can be used to reverse the order of items. The order of insertion is the reverse of the order of removal.   
**Order: LIFO (last in,first out 后进先出)**    
## Abstract Data Type  
* `Stack()` creates a new stack that is empty. It needs no parameters and returns an empty stack.  
* `push(item)` adds a new item to the top of the stack. It needs the item and returns nothing.  
* `pop()` removes the top item from the stack. It needs no parameters and returns the item. The stack is modified.  
* `peek()` returns the top item from the stack but does not remove it. It needs no parameters. The stack is not modified.  
* `isEmpty()` tests to see whether the stack is empty. It needs no parameters and returns a boolean value.  
* `size()` returns the number of items on the stack. It needs no parameters and returns an integer.   
 
we need only to decide which end of the list will be considered the top of the stack and which will be the base. Once that decision is made, the operations can be implemented using the list methods such as append and pop.(O(1))  
The following stack implementation  assumes that the end of the list will hold the top element of the stack：  
``` 
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)  
```
## problems：  
1. balanced symbols符号匹配    
2. converting decimal nums to binary nums (Divide by 2 algorithm，reverse order) general case：any base(digits = “0123456789ABCDEF”,eg:base:16) 转化十进制为2(或其他)进制  
3. infix ,prefix and postfix 前缀，中缀与后缀  
4. 图的depth search（DFS)  
