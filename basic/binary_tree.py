from TreeNode import TreeNode as Node

class BinaryTree:
  def __init__(self):
    self.root = None

  def add(self, node = None):
    if node is None:
      return False

    if self.root is None:
      self.root = node
      self.height = 1
      self.size = 1
      return True

    temp = self.root
    while temp:
      if temp.data < node.data:
        if temp.right is None:
          temp.right = node
          return True
        else:
          temp = temp.right
      else:
        if temp.left is None:
          temp.left = node
          return True
        else:
          temp = temp.left

    return False

  def find(self, target):
    if target is None:
      return None

    temp = self.root
    while temp:
      if temp.data < target.data:
        temp = temp.right
      elif temp.data < target.data:
        temp = temp.left
      else:
        return temp

    print 'NOT FOUND!'
    return None

  def preOrder(self, node = None):
    if node is None:
      return None

    print node.data,
    self.preOrder(node.left)
    self.preOrder(node.right)

  def preOrderIt(self):
    if not self.root:
      print 'EMPTY TREE'
      return None

    stack = [self.root]
    while stack:
      node = stack.pop()
      print node.data,
      if node.right:
        stack.append(node.right)
      if node.left:
        stack.append(node.left)

  def inOrder(self, node = None):
    if node is None:
      return None

    self.inOrder(node.left)
    print node.data,
    self.inOrder(node.right)

  def postOrder(self, node = None):
    if node is None:
      return None

    self.postOrder(node.left)
    self.postOrder(node.right)
    print node.data,

  def levelOrder(self):
    if not self.root:
      print 'EMPTY TREE'
      return None

    queue = [self.root]
    while queue:
      node = queue.pop(0)
      print node.data,
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)

  def getHeight(self, node = None):
    if node is None:
      return 0

    return 1 + max(self.getHeight(node.left), self.getHeight(node.right))

  def LCA(self, a, b, node = None):
    if not node:
      return None

    if a == node.data or b == node.data:
      return node

    l = self.LCA(a, b, node.left)
    r = self.LCA(a, b, node.right)

    if l and r:
      print node.data
      return node

    if l:
      return l

    if r:
      return r


if __name__ == '__main__':
  t = BinaryTree()
  t.add(Node(5))
  t.add(Node(2))
  t.add(Node(1))
  t.add(Node(3))
  t.add(Node(4))
  t.add(Node(7))
  t.add(Node(6))
  t.add(Node(8))
  t.preOrder(t.root)
  print '\n======='
  t.preOrderIt()
  print '\n======='
  t.inOrder(t.root)
  print '\n======='
  t.postOrder(t.root)
  print '\n======='
  t.levelOrder()
  print '\n======='
  print t.getHeight(t.root)
  print '======='
  t.LCA(6, 4, t.root)
