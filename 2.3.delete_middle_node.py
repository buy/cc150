from Node import *
from LinkedList import *

def deleteMiddleNode(node):
  if node is None:
    return None

  if node.next:
    node.data = node.next.data
    node.next = node.next.next
  else:
    node.data = None
    node.next = None

if __name__ == '__main__':
  nodes = [Node(i) for i in range(10)]
  nodes.extend([Node(3), Node(5)])
  nodes.insert(1, Node(8))

  linkedlist = LinkedList()
  for node in nodes:
    linkedlist.addNode(node)
  print linkedlist

  middileNode = linkedlist.head
  for i in range(5):
    middileNode = middileNode.next

  print middileNode

  # start your funciton here
  deleteMiddleNode(middileNode)
  print linkedlist
