from Node import Node

class LinkedList:
  def __init__(self, headNode = None):
    self.head = headNode
    self.length = 1 if headNode else 0

  def __str__(self):
    return ' -> '.join(str(node.data)
                      for node in self.resultGenerator())

  def resultGenerator(self):
    currentNode = self.head
    while currentNode:
      yield currentNode
      currentNode = currentNode.next

  def addNode(self, newNode=None):
    if newNode is None:
      return None

    if self.head is None:
      self.head = newNode
      return self.head

    temp = self.head

    while temp.next:
      temp = temp.next

    temp.next = newNode
    self.length += 1

    return self.head

  def removeNode(self, curNode):
    if curNode is None:
      return self.head

    temp = self.head

    while temp.next:
      if temp.next.data == curNode.data:
        temp.next = temp.next.next
        self.length -= 1
        return self.head

      temp = temp.next

    return self.head

  def findNode(self, targetNode):
    if targetNode is None:
      return None

    temp = self.head

    while temp.next:
      if temp.next.data == targetNode.data:
        return temp.next

      temp = temp.next

    return None

if __name__ == '__main__':
  n1 = Node(1)
  print n1
  ln1 = LinkedList(n1)
  print ln1.length
  ln1.addNode(Node(8))
  print ln1
  n2 = Node(5)
  ln1.addNode(n2)
  print ln1
  n2 = Node(15)
  ln1.addNode(n2)
  print ln1

  ln2 = LinkedList()
  ln2.addNode()
  print '>' + str(ln2)
  ln2.addNode(n2)
  print vars(ln2.head)
  print '>' + str(ln2)
  ln2.addNode(Node(100))
  print '>' + str(ln2)
