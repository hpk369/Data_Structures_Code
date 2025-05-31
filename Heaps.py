class MinBinaryHeap():

  def __init__(self):
    self.heap = [1,3,5,9,8]

  def get_parent(self, index):
    if index == 0:
      return None
    return self.heap[(index-1) // 2]
  
  def set_parent(self, index, val):
    if index == 0:
      return None
    self.heap[(index-1) // 2] = val

  def get_left_child(self, index):
    left_child_index = 2 * index + 1
    if left_child_index <= self.size() - 1:
      return self.heap[left_child_index]
    else:
      return None
    
  def set_left_child(self, index, val):
    left_child_index = 2 * index + 1
    if left_child_index <= self.size() - 1:
      self.heap[left_child_index] = val

  def get_right_child(self, index):
    right_child_index = 2 * index + 2
    if right_child_index <= self.size() - 1:
      return self.heap[right_child_index]
    else:
      return None
    
  def set_right_child(self, index, val):
    right_child_index = 2 * index + 2
    if right_child_index <= self.size() - 1:
      self.heap[right_child_index] = val

  def size(self):
    return len(self.heap)
  
  def insert(self, val):
    # Add the new value to the end of the heap
    self.heap.append(val)
    # Call _heapify_up to maintain the heap property
    self._heapify_up(len(self.heap) - 1)

  def _heapify_up(self, index):
    # while the index is not at the root (index > 0)
    while index > 0:
      # Calculate the index of the parent node
      parent_index = (index-1) // 2
      # If the value at the current index is less than its parent's value
      if self.heap[index] < self.get_parent(index):
        # Swap the values between the current node and its parent
        self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
        # Move up to the parent node
        index = parent_index
      else:
        # If the current node is in the correct position, break the loop
        break

  def extract_mins(self):
    # If the heap is empty, return None
    if len(self.heap) == 0:
      return None
    # If there's only one element in the heap, remove amd return it
    if len(self.heap) == 1:
      return self.heap.pop()
    
    # Store the minimum value (root) before removal
    min_val = self.heap[0]
    # Replace the root with the last element in the heap
    self.heap[0] = self.heap.pop()
    # Restore the heap property by moving down the root value
    self._heapify_down(0)
    # Return the minimum value that was extracted
    return min_val
  
  def _heapify_down(self, index):
    # Calculate the indices of the left and right children of the current node
    left_child_index = 2 * index + 1
    right_child_index = 2 * index + 2
    # Initialize the index of the smallest value as the current node's index
    smallest = index

    # Check if the left child exists and its value is smaller than the current smallest value
    if(left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]):
      smallest = left_child_index
    # Check if the right child exists and its value is smaller than the current smallest value
    if(right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]):
      smallest = right_child_index

    # If the smallest value is not at the current node (i.e., it's one of the children)
    if smallest != index:
      # Swap the values between the current node and the smallest child
      self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
      # Recursively call the _heapify_down on the swapped child to restore the heap property
      self._heapify_down(smallest)

  def get_min(self):
    if len(self.heap) == 0:
      return None
    return self.heap[0]


h = MinBinaryHeap()

# h.extract_mins()
print(h.get_min())