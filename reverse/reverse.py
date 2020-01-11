class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node
    # print(self.head.value)

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):
    # TO BE COMPLETED
    prev = None
    curr = self.head
    nxt = None

    while curr:
      print(f'current: {curr.value}')
      nxt = curr.next_node # assign nxt to be the current's next node
      curr.next_node = prev # set the next node to the current's previous node
      prev = curr # set prev to be the current node, when it moves to the next iteration, it will use this "current" now prev as it's next node
      curr = nxt # set curr to be the next node and continue while loop

    self.head = prev

arr = LinkedList()
arr.add_to_head(3)
arr.add_to_head(5)
arr.add_to_head(7)
arr.add_to_head(9)

arr.reverse_list()