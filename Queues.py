class Queue():

  def __init__(self, limit=10):
    self.queue = []
    self.front = None
    self.rear = None
    self.limit = limit

  def isEmpty(self):
    return len(self.queue)<=0
  
  def enqueue(self, data):
    if len(self.queue) >= self.limit:
      return print("queue is at limit")
    else:
      self.queue.append(data)

    # assign the rear as size of the queue and front as 0
    if self.front is None:
      self.front = self.rear = 0
    else:
      self.rear = len(self.queue)-1

  # to pop an element from the front-end of the queue
  def dequeue(self):
    if self.isEmpty():
      return print("queue is empty")
    else:
      self.queue.pop(0)
      if len(self.queue) == 0:
        self.front = self.rear = None
      else:
        self.rear = len(self.queue)-1

  def peek(self):
    return self.front
    
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.queue[q.rear])
q.peek()