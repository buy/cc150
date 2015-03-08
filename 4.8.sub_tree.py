# 10:26

def isSubTree(t1, t2):
  if t2 is None:
    return True

  return hasSubTree(t1, t2)

def hasSubTree(r1, r2):
  if r1 is None:
    return False

  if r1.data == r2.data:
    if isMatchTree(r1, r2):
      return True

  return hasSubTree(r1.left, r2) or hasSubTree(r1.right, r2)

def isMatchTree(r1, r2):
  if r1 is None and r2 is None:
    return True

  if r1 is None or r2 is None:
    return False

  if r1.data == r2.data:
    return isMatchTree(r1.left, r2.left) and isMatchTree(r1.right, r2.right)

  return False


if __name__ == '__main__':
  print isSubTree(t1, t2)
