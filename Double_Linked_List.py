class Node():

  def __init__(self, data, next=None, previous=None):
    self.data = data
    self.next = next
    self.prev = previous


class DoublyLinkedList():

  def __init__(self):
    self.head = None

  def insertNodeAtHead(self, new_node):
    if self.head == None:
      self.head = new_node
    else:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node

  def insertNodeAtEnd(self, new_node):
    current_node = self.head
    while(current_node.next):
      current_node = current_node.next
    current_node.next = new_node
    new_node.prev = current_node

  def insertNodeAtMiddle(self, target_node, new_node):
    if(target_node.next is None):
      return print("try inserting at end")
    else:
      new_node.next = target_node.next
      new_node.prev = target_node

      target_node.next.prev = new_node
      target_node.next = new_node

  def printLinkedList(self):
    current_node = self.head
    while(current_node):
      print(current_node.data)
      current_node = current_node.next

  def searchByData(self, target_data = None):
    if(not target_data):
      return print("no data passed in")
    
    current_node = self.head
    while(current_node):
      if(current_node.data == target_data):
        return current_node
      current_node = current_node.next

  def deleteHead(self):
    if(self.head is None):
      print('This list is already empty')
    else:
      current_node = self.head
      self.head = current_node.next
      current_node = None

  def deleteGivenNode(self, target_data):
    current_node = self.head
    if(current_node.data == target_data):
       return self.deleteHead()

    previous_node = None

    # traverse list until target found or end
    while(current_node and current_node.data != target_data):
      current_node = current_node.next

    if current_node is None:
      print('data not found')
      return
    
    current_node.prev.next = current_node.next
    if current_node.next is not None:
      current_node.next.prev = current_node.prev

doubly_linked_list = DoublyLinkedList()
ten = Node(10)
twenty = Node(20)
thirty = Node(30)
five = Node(5)
fifty = Node(50)
doubly_linked_list.insertNodeAtHead(ten)
doubly_linked_list.insertNodeAtEnd(five)
doubly_linked_list.insertNodeAtMiddle(ten, thirty)
doubly_linked_list.insertNodeAtMiddle(thirty, twenty)
doubly_linked_list.printLinkedList()


