def next(node=None):
  if node is None:
    return None

  if node.right:
    return findLeftMost(node.right)
  else:
    return findNextParent(node)

def findLeftMost(node=None):
  if root is None:
    return None

  temp = node

  while temp.left:
    temp = temp.left

  return temp

def findNextParent(node=None):
  if node is None:
    return None

  p = node.parent
  temp = node

  while p and p.left is not temp:
    p = p.parent
    temp = temp.parent

  return p
