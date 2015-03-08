class Queue:
  def __init__(self):
    self.oldStack = []
    self.newStack = []

  def __str__(self):
    stack = self.oldStack + self.newStack[::-1]
    if stack:
      return ' -> '.join(str(i) for i in stack)
    else:
      return 'Empty Stack!'

  def _shiftStack(self):
    if self.oldStack == []:
      self.oldStack = self.newStack[::-1]
      self.newStack = []

  def append(self, data):
    self.newStack.append(data)

  def dequeue(self):
    self._shiftStack()
    if self.oldStack:
      return self.oldStack.pop()
    else:
      return None

  def peek(self):
    self._shiftStack()
    return self.oldStack[-1]


if __name__ == '__main__':
  q = Queue()
  q.append(1)
  q.append(2)
  print 'peek!'
  print q.peek()
  q.append(3)
  print q.peek()
  print q.dequeue()
  print q
  print q.dequeue()
  print q.dequeue()
  print q.dequeue()
  print q
