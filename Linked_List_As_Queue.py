class Node:

  def __init__(self,data):
    self.data = data
    self.next = None


class Queue:

  def __init__(self):
    self.front = None
    self.rear = None

  def is_Empty(self):
    return self.front == None
  
  def enqueue(self, data):
    temp = Node(data)
    
    if self.is_Empty():
      self.front = self.rear = temp
      return 
    else:
      self.rear.next = temp
      self.rear = temp

  def dequeue(self):
    if self.is_Empty():
      return print("queue is empty")
    
    temp = self.front
    self.front = temp.next
    temp = None

    if(self.front == None):
      self.rear = None
