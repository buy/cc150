"""
6:24
"""
class Node:
  def __init__(self, data=None):
    self.data = data
    self.left = None
    self.right = None

  def __str__(self):
    output = []
    self.inOrder(self, output)
    return str(output)

  def inOrder(self, root=None, result=[]):
    if not root:
      return None

    self.inOrder(root.left, result)
    result.append(root.data)
    self.inOrder(root.right, result)

def arrayToBinary(array, low=0, high=None):
  if not array:
    return None

  if high is None:
    high = len(array)-1

  if low > high:
    return None

  mid = (high + low) / 2

  root = Node(array[mid])
  root.left = arrayToBinary(array, low, mid-1)
  root.right = arrayToBinary(array, mid+1, high)

  return root


if __name__ == '__main__':
  a = [1,2,3,4,6,7]
  tree = arrayToBinary(a)
  print tree
