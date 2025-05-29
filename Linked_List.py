class Node():

  def __init__(self, data, next=None):
    self.data = data
    self.next = next

  def getData(self):
    return self.data
  
  def setData(self, data):
    self.data = data

  def getNext(self):
    return self.next
  
  def setNext(self, next):
    self.next = next


class LinkedList():

  def __init__(self):
    self.head = None

  def insertNodeAtHead(self, new_node):
    if self.head == None:
      self.head = new_node
    else:
      new_node.setNext(self.head)
      self.head = new_node

  def insertNodeAtEnd(self, new_node):
    current_node = self.head
    while(current_node.next):
      current_node = current_node.next
    current_node.setNext(new_node)

  def insertNodeAtMiddle(self, target_node, new_node):
    if(target_node.getNext() is None):
      return print("try inserting at end")
    else:
      new_node.setNext(target_node.next)
      target_node.setNext(new_node)

  def printLinkedList(self):
    current_node = self.head
    while(current_node):
      print(current_node.data)
      current_node = current_node.next

  def searchByData(self, target_data):
    if(not target_data):
      return print("no data passed in")
    
    current_node = self.head
    while(current_node):
      if(current_node.getData() == target_data):
        return current_node
      current_node = current_node.getNext()

  def deleteHead(self):
    current_node = self.head
    self.head = current_node.getNext()
    current_node = None

  def deleteGivenNode(self, target_data):
    current_node = self.head
    if(current_node.getData() == target_data):
       return self.deleteHead()

    previous_node = None

    # traverse list until target found or end
    while(current_node and current_node.getData()!=target_data):
      previous_node = current_node
      current_node = current_node.getNext()

    if current_node is None:
      return print('data not found')
    
    else:
      previous_node.setNext(current_node.getNext())
    

linked_list = LinkedList()
five = Node(5)
ten = Node(10)
fifteen = Node(15)
twenty = Node(20)
linked_list.insertNodeAtHead(ten)
linked_list.insertNodeAtHead(five)
linked_list.insertNodeAtEnd(fifteen)
linked_list.insertNodeAtEnd(twenty)
linked_list.insertNodeAtMiddle(ten, Node(25))
linked_list.printLinkedList()
linked_list.deleteGivenNode(20)
linked_list.printLinkedList()