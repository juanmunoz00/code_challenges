from icecream import ic

class Nodes:
  def __init__(self, value, nextNode = None):
    self.value = value
    self.nextNode = nextNode

class LinkedList:
  def __init__(self, head = None):
    self.head = head

  """
  This method instantiates the Nodes class and inserts the value at the end of the linked list.
  """
  def insert(self, value):
    try:

      newNode = Nodes(value)
      # If the linked list is empty, the new node becomes the head.
      if self.head is None:
        self.head = newNode
        return
        
      # Otherwise, we traverse the linked list until we reach the last node.
      currentNode = self.head
      while True:
        if currentNode.nextNode is None:
          currentNode.nextNode = newNode
          break
        currentNode = currentNode.nextNode


    except Exception as e: print(e)

  """
    This methos prints the linked list.
  """
  def PrintLinkedList(self):
    try:
      currentNode = self.head
      while currentNode is not None:
        print(currentNode.value, end = " -> ")
        currentNode = currentNode.nextNode

      print("None")
      
    except Exception as e: print(e)