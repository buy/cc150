from Node import *
from LinkedList import *

def partitionList(linkedlist, target):
  if linkedlist is None:
    return None

  smallStart = smallEnd = largeStart = largeEnd = None
  node = linkedlist.head

  while node:
    if node.data < target:
      if not smallStart:
        smallStart = smallEnd = node
      else:
        smallEnd.next = node
        smallEnd = smallEnd.next
    else:
      if not largeStart:
        largeStart = largeEnd = node
      else:
        largeEnd.next = node
        largeEnd = largeEnd.next
    node = node.next

  if smallEnd is None:
    return linkedlist(largeStart)

  smallEnd.next = largeStart

  return LinkedList(smallStart)

if __name__ == '__main__':
  nodes = [Node(i) for i in range(10)]
  nodes.extend([Node(3), Node(5)])
  nodes.insert(1, Node(8))

  linkedlist = LinkedList()
  for node in nodes:
    linkedlist.addNode(node)
  print linkedlist

  print partitionList(linkedlist, 5)
