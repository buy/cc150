class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None

def findStart(ls):
  slow = fast = ls

  while slow is not None and fast is not None:
    slow = slow.next
    fast = fast.next.next

    if slow is fast:
      break

  slow = ls

  while slow is not fast:
    slow = slow.next
    fast = fast.next

  return slow


if __name__ == '__main__':
  tail = ls = Node('A')
  tail.next = Node('B')
  tail = tail.next
  target = tail.next = Node('C')
  tail = tail.next
  tail.next = Node('D')
  tail = tail.next
  tail.next = Node('E')
  tail = tail.next
  tail.next = target

  print findStart(ls).data
