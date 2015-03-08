from Node import *
from LinkedList import *

def findKthLast(linkedlist, k):
  """k is 1 based
  """
  if linkedlist is None or linkedlist.head is None:
    return None

  fast = slow = linkedlist.head
  k -= 1

  while k and fast.next:
    fast = fast.next
    k -=1

  if k != 0:
    return None

  while fast.next:
    fast = fast.next
    slow = slow.next

  return slow


if __name__ == '__main__':
  nodes = [Node(i) for i in range(10)]
  nodes.extend([Node(3), Node(5)])
  nodes.insert(1, Node(8))

  linkedlist = LinkedList()
  for node in nodes:
    linkedlist.addNode(node)
  print linkedlist
  print findKthLast(linkedlist, 3)
