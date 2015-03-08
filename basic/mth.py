class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def setHead(self, node):
    if node is None:
      return None

    self.head = node

    return self.head

  def findTail(self):
    temp = self.head
    if not temp:
      return None

    while temp.next:
      temp = temp.next

    return temp

  def show(self):
    temp = self.head
    if not temp:
      return None

    while temp.next:
      print temp
      temp = temp.next

    return None

  def append(self, node):
    if not self.head:
      self.head = node
    else:
      temp = self.head
      while temp.next:
        temp = temp.next

      temp.next = node

def findMth(node, m):
  if not node:
    return None

  fast = slow = node

  for i in range(m - 1):
    if fast.next:
      fast = fast.next
    else:
      return None

  while fast.next:
    fast = fast.next
    slow = slow.next

  return slow


if __name__ == '__main__':
  n1 = Node(5)
  n2 = Node(4)
  n3 = Node(3)
  n4 = Node(2)
  n5 = Node(1)
  n1.next = n2
  n2.next = n3
  n3.next = n4
  n4.next = n5

  print findMth(n1, 5)
