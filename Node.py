class Node:
  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next

  def __str__(self):
    return '{ data: ' + str(self.data) + ' | next: ' + str(self.next) + ' }'

  def setNext(self, node=None):
    if node is None:
      return None

    self.next = node

    return self

if __name__ == '__main__':
  n1 = Node(1)
  n0 = Node(0, n1)
  print n0
  print n1
  n2 = Node(2)
  n1.setNext(n2)
  print n0
