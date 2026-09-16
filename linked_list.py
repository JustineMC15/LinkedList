class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self, value):
    new_node = Node(value)
    self.head = new_node
    self.tail = new_node
    self.length = 1

  def print_list(self):
    if self.length == 0:
      return False
    temp = self.head
    while temp is not None:
      print(temp.value)
      temp = temp.next

  def append(self,value):
    new_node = Node(value)
    if self.length == 0:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
    self.length += 1
    return new_node.value

  def prepend(self, value):
    new_node = Node(value)
    if self.length == 0:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head = new_node
    self.length += 1
    return new_node.value

  def pop_first(self):
    if self.length == 0:
      return False
    temp = self.head
    if self.length == 1:
      self.head = None
      self.tail = None
    else:
      self.head = temp.next
      temp.next = None
    self.length -= 1
    return temp.value

  def get(self, index):
    if self.length == 0 or index < 0 or index >= self.length:
      return None
    temp = self.head
    for i in range(index):
      temp = temp.next
    return temp

  def pop(self):
    if self.length == 0:
      return False
    if self.length == 1:
      return self.pop_first()
    target = self.tail
    temp = self.get(self.length - 2)
    temp.next = None
    self.tail = temp
    self.length -= 1
    return target.value

  def insert(self, index, value):
    if index < 0 or index > self.length:
      return False
    if index == 0:
      return self.prepend(value)
    elif index == self.length:
      return self.append(value)
    else:
      new_node = Node(value)
      temp = self.get(index - 1)
      target = temp.next
      temp.next = new_node
      new_node.next = target
      self.length += 1
      return new_node.value

  def remove(self, index):
    if index < 0 or index >= self.length:
      return False
    if index == 0:
      return self.pop_first()
    elif index == self.length - 1:
      return self.pop()
    else:
      temp = self.get(index - 1)
      target = temp.next
      temp.next = target.next
      self.length -= 1
      return target.value
  
  def reverse(self):
    if self.length <= 1:
      return False
    current = self.head
    oldhead = current
    before = None
    while current is not None:
      after = current.next
      current.next = before
      before = current
      current = after
    self.head = before
    self.tail = oldhead
        
my_linked_list = LinkedList(15)
my_linked_list.append(20)
my_linked_list.prepend(10)
my_linked_list.append(25)
my_linked_list.prepend(5)
my_linked_list.print_list()
print("Reversing Now")
my_linked_list.reverse()
my_linked_list.print_list()
print("Now adding a value in index 3")
my_linked_list.insert(1,3)
my_linked_list.print_list()
print("Removing 3 from index 1")
my_linked_list.remove(1)
my_linked_list.print_list()
print("Call pop and pop_first")
my_linked_list.pop()
my_linked_list.pop_first()
my_linked_list.print_list()
print("Prepend and append new values")
my_linked_list.append(210)
my_linked_list.prepend(2)
my_linked_list.print_list()
print("Reversing Now")
my_linked_list.reverse()
my_linked_list.print_list()
