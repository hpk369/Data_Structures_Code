class PriorityQueue():

  def __init__(self):
    self.queue = []

  def insert(self, data):
    self.queue.append(data)

  def remove(self):
    if not self.queue:
      if not self.queue:
        return
      else:
        # Find the item with highest priority
        highest_priority_index = self.__get_index_of_highest_priority_item()
        
  def peek(self):
    if not self.queue:
      return
    else:
      # Find the item with highest priority
      highest_priority_index = self.__get_index_of_highest_priority_item()
      return self.queue[highest_priority_index][0]
    
  def update_priority(self, target_value, new_priority):
    if not self.queue:
      return
    for i in self.queue:
      if i[0] == target_value:
        i[1] = new_priority
        return
      
      return print("item not found")

  def __get_index_of_highest_priority_item(self):
    highest_priority_index = 0
    for i in range(0, len(self.queue)):
      if self.queue[i][1] > self.queue[highest_priority_index][1]:
        highest_priority_index = i
    return highest_priority_index


pq = PriorityQueue()
pq.insert(["Task 1", 10])
pq.insert(["Task 2", 5])
pq.insert(["Task 3", 20])
print(pq.peek())