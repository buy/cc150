from basic import *

def inOrder(root = None, array = None):
  if root is None or array is None:
    return None

  inOrder(root.left, array)
  array.append(root)
  inOrder(root.right, array)

def bstToLinkedlist(root = None):
  if not root:
    return None

  array = []
  inOrder(root, array)

  array[0].left = None
  for i in range(1, len(array)):
    array[i].left = array[i - 1]
    array[i - 1].right = array[i]

  array[-1].right = None

  return array

if __name__ == '__main__':
  t = BinaryTree()
  root = Node(5)
  t.add(root)
  t.add(Node(2))
  t.add(Node(1))
  t.add(Node(3))
  t.add(Node(4))
  t.add(Node(7))
  t.add(Node(6))
  t.add(Node(8))
  t.inOrder(t.root)
  print '\n======='

  a = bstToLinkedlist(root)
  # print a
  n = a[0]
  while n:
    print n.data,
    n = n.right
