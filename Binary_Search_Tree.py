class Node:

  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data


class BinarySearchTree:

  def __init__(self):
    self.root = None

  def insert(self, data):
    if self.root is None:
      self.root = Node(data)
    else:
      self._insert_recursive(self.root, data)
  
  def _insert_recursive(self, current, data):
    if data < current.data:
      if current.left is None:
        current.left = Node(data)
      else:
        self._insert_recursive(current.left, data)
      
    else: # Assuming no duplicates
      if current.right is None:
        current.right = Node(data)
      else:
        self._insert_recursive(current.right, data)
  
  def inorder_traversal(self):
    self._inorder_recursive(self.root)
  
  def _inorder_recursive(self, current):
    if current is not None:
      self._inorder_recursive(current.left)
      print(current.data, end=' ')
      self._inorder_recursive(current.right)

  def search(self, data):
    return self._search_recursive(self.root, data)
  
  def _search_recursive(self, current, data):
    if current.data == data or current is None:
      return current
    
    if data < current.data:
      self._search_recursive(current.left, data)
    
    else:
      self._search_recursive(current.right, data)

  def find_min(self):
    current = self.root
    while current.left:
      current = current.left
    return current
  
  def find_max(self):
    current = self.root
    while current.right:
      current = current.right
    return current

  def delete(self, data):
    self.root = self._delete_recursive(self.root, data)

  def _delete_recursive(self, current, data):
    if current is None:
      return current
    
    # If the data to be deleted is smaller than the current node's data, then it lies in the left subtree
    elif current.data > data:
      current.left =  self._delete_recursive(current.left, data)
    
    # If the data to be deleted is larger than the current node's data, then it lies in the right subtree
    elif current.data < data:
      current.right =  self._delete_recursive(current.right, data)

    # If the data matches, then this node needs to be deleted
    else:
      # Case-1 Node with no children
      if current.left is None and current.right is None:
        return None
      # Case-2 Node with one children
      elif current.left is None:
        return current.right
      elif current.right is None:
        return current.left
      # Case-3 Node with two children
      else:
        # Get the inorder successor (smallest in right subtree)
        temp = self._find_min_node(current.right)
        # Copy the inorder successor to this node
        current.data = temp.data
        # Delete the inorder succesor
        current.right = self._delete_recursive(current.right, temp.data)

    return current

  def _find_min_node(self, node):
    current = node
    while current.left:
      current = current.left
    return current

# Example Usage
bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)
bst.insert(9)
bst.delete(7)

bst.inorder_traversal()