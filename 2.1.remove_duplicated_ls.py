from Node import *
from LinkedList import *

def removeDuplicate(linkedlist):
  if linkedlist.head is None:
    return None

  temp = linkedlist.head
  nodeMap = {temp.data: True}

  while temp.next:
    if temp.next.data in nodeMap:
      temp.next = temp.next.next
    else:
      nodeMap[temp.data] = True
      temp = temp.next

  return linkedlist

if __name__ == '__main__':
  nodes = [Node(i) for i in range(10)]
  nodes.extend([Node(3), Node(5)])
  nodes.insert(1, Node(8))

  linkedlist = LinkedList()
  for node in nodes:
    linkedlist.addNode(node)

  print linkedlist
  print removeDuplicate(linkedlist)

  
