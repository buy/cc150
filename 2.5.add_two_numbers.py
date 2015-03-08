class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None

  def __str__(self):
    output = []
    while self:
      output.append(str(self.data))
      self = self.next

    return ' -> '.join(output)

def add(nodes1, nodes2):
  carry = 0
  output = None

  while nodes1 and nodes2:
    if not output:
      output = Node((nodes1.data + nodes2.data) % 10)
      temp = output
    else:
      temp.next = Node((carry + nodes1.data + nodes2.data) % 10)
      temp = temp.next

    if (nodes1.data + nodes2.data) / 10 > 0:
      carry = 1
    else:
      carry = 0

    nodes1 = nodes1.next
    nodes2 = nodes2.next

  while nodes1:
    temp.next = Node((carry + nodes1.data) % 10)
    temp = temp.next

    if ((carry + nodes1.data) / 10) > 0:
      carry = 1
    else:
      carry = 0

    nodes1 = nodes1.next

  while nodes2:
    temp.next = Node((carry + nodes2.data) % 10)
    temp = temp.next
    if ((carry + nodes2.data) / 10) > 0:
      carry = 1
    else:
      carry = 0

    nodes2 = nodes2.next

  if carry:
    temp.next = Node(1)    

  return output


if __name__ == '__main__':
  ls1 = Node(7)

  ls2 = Node(5)
  ls2.next = Node(9)
  ls2.next.next = Node(2)

  print '`{ls1}` + `{ls2}`'.format(ls1=ls1, ls2=ls2)
  print add(ls1, ls2)


