# 11:45

class Node:
  def __init__(self, data=None):
    self.data = data
    self.left = None
    self.right = None

def findLCA(node1, node2, root):
  if root is None:
    return None

  if node1 is root or node2 is root:
    return root

  l = findLCA(node1, node2, root.left)
  r = findLCA(node1, node2, root.right)

  if l and r:
    return root

  if l:
    return l

  if r:
    return r

if __name__ == '__main__':
  node1 = Node(2)
  node2 = Node(1)
  node3 = Node(3)
  node4 = Node(5)
  node5 = Node(6)
  node6 = Node(7)
  node7 = Node(8)
  node8 = Node(12)
  node1.left = node2
  node1.right = node3
  node2.left = node4
  node2.right = node5
  node5.right = node8
  node3.left = node6
  node3.right = node7

  print findLCA(node1, node3, node1).data
  # print findLCA(None, None, None).data
  print findLCA(node8, node4, node1).data
  print findLCA(node8, node5, node2).data
  print findLCA(node6, node7, node1).data



 #      2
 #    /   \
 #   1     3
 #  / \   / \
 # 5   6 7   8
 #      \
 #       12
