class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    self.top = None

  def __str__(self):
    if not self.top:
      return 'Stack is Empty!'

    node = self.top
    output = []
    while node:
      output.append(node.data)
      node = node.next

    return str(output)

  def push(self, data):
    if not self.top:
      self.top = Node(data)
    else:
      node = Node(data)
      node.next = self.top
      self.top = node

  def top(self):
    return self.top

  def pop(self):
    node = self.top
    if self.top.next:
      self.top = self.top.next
    else:
      self.top = None

    return node

  def deleteStack(self):
    self.top = None


if __name__ == '__main__':
  st = Stack()
  print st
  st.push(1)
  print st
  st.push(3)
  print st
  st.push(-1)
  print st
  st.deleteStack()
  print st
