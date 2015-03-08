from basic import *

def getTreeHeight(root):
  if root is None:
    return 0

  return 1 + max(getTreeHeight(root.left), getTreeHeight(root.right))

def isBalancedTree(root):
  if root is None:
    return True

  if abs(getTreeHeight(root.left) - getTreeHeight(root.right)) > 1:
    return False
  else:
    return isBalancedTree(root.left) and isBalancedTree(root.right)

if __name__ == '__main__':
  t = BinaryTree()
  t.add(Node(5))
  t.add(Node(2))
  t.add(Node(1))
  t.add(Node(-1))
  t.add(Node(-2))
  t.add(Node(-3))
  t.add(Node(3))
  t.add(Node(4))
  t.add(Node(7))
  t.add(Node(6))
  t.add(Node(8))
  t.preOrder(t.root)
  print
  print '---'
  print getTreeHeight(t.root)
  print getTreeHeight(None)
  print isBalancedTree(t.root)
  print isBalancedTree(None)
