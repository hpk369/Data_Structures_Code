class Stack():
  def __init__(self, limit = 10):
    self.stack = []
    self.limit = limit
  
  def push(self, data):
    if len(self.stack) >= self.limit:
      return print('Stack Overflow')
    else:
      self.stack.append(data)
    
  def printStack(self):
    return print(self.stack)
  
  def pop(self):
    if len(self.stack) > 0:
      return self.stack.pop()
    else:
      return print("empty stack")
    
  def peek(self):
    if len(self.stack) > 0:
      return self.stack[-1]
    else:
      return print("empty stack")
    

    

stack = Stack()
stack.push(2)
stack.push(5)
stack.pop()
stack.printStack()
stack.pop()
stack.peek()