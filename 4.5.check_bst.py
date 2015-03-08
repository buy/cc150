# 10:02
class Node:
  def __init__(self, data=None):
    self.data = data
    self.left = None
    self.right = None

class Tree:
  def __init__(self):
    self.root = None

  def add(self, node=None):
    if node is None:
      return False

    if self.root is None:
      self.root = node
      return self.root

    temp = self.root
    while temp:
      if node.data <= temp.data:
        if temp.left is None:
          temp.left = node
          return True
        else:
          temp = temp.left
      else:
        if temp.right is None:
          temp.right = node
          return True
        else:
          temp = temp.right

    return False

def isBST(root=None):
  if root is None:
    return True

  treeNodes = []
  inOrder(root, treeNodes)

  return checkIncrease(treeNodes)

def checkIncrease(array):
  for i in range(1, len(array)):
    if array[i-1] > array[i]:
      return False

  return True

def inOrder(root=None, outputs=[]):
  if root is None:
    return None

  inOrder(root.left, outputs)
  outputs.append(root.data)
  inOrder(root.right, outputs)


if __name__ == '__main__':
  tree = Tree()
  tree.add(Node(2))
  tree.add(Node(1))
  tree.add(Node(3))
  tree2 = Tree()
  tree2.root = Node(11)
  tree2.root.left = Node(55)
  tree2.root.right = Node(1111)
  print isBST(tree.root)
  print isBST(tree2.root)
