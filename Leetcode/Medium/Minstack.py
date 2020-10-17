### https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []
        

    def push(self, x: int) -> None:
        
        if self.isEmpty():
            self.stack.append(x)
            self.min_stack.append(x)
            return
        
        if x <= self.min_stack[-1]:
            self.min_stack.append(x)
        
        self.stack.append(x)
        return
               
    def pop(self) -> None:
        
        if self.isEmpty():
            print("Cannot pop from an empty stack.")
            return
        
        if self.min_stack[-1] == self.stack[-1]:
            self.min_stack.pop()
        
        self.stack.pop()
        
    def top(self) -> int:
        if self.isEmpty():
            print("Stack is empty, no top element found!")
            return
        
        return self.stack[-1]

    def getMin(self) -> int:
        
        return self.min_stack[-1]
    
    def isEmpty(self):
        return not self.stack
        
    

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()