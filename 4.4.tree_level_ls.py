# 8:47
from basic import *

class Node:
  def __init__(self, data=None):
    self.data = data
    self.left = None
    self.right = None

def getLinkedList(root=None):
  if root is None:
    return None

  level = 0
  root.level = level
  queue = [root]
  output = []
  levelOutput = []

  while queue:
    temp = queue.pop(0)
    if temp.level > level:
      level = temp.level
      output.append(levelOutput)
      levelOutput = []
      levelOutput.append(temp.data)
    else:
      levelOutput.append(temp.data)

    if temp.left:
      temp.left.level = level + 1
      queue.append(temp.left)

    if temp.right:
      temp.right.level = level + 1
      queue.append(temp.right)

  if levelOutput:
    output.append(levelOutput)

  return output



if __name__ == '__main__':
  t = BinaryTree()
  t.add(Node(5))
  t.add(Node(3))
  t.add(Node(1))
  t.add(Node(4))
  t.add(Node(8))

  list = getLinkedList(t.root)
  print list


  


