class Stack:
  def __init__(self):
    self.data = []

  def __str__(self):
    return str(self.data)

  def append(self, data):
    self.data.append(data)
    return self.data[-1]

  def pop(self):
    if not self.data:
      print 'Can not pop from empty stack!'

    return self.data.pop()

  def peek(self):
    if not self.data:
      print 'Can not peek empty stack!'

    return self.data[-1]

  def sort(self):
    if not self.data:
      print 'Can not sort on empty stack!'

    tempStack = Stack()

    while self.data:
      temp = self.data.pop()

      while tempStack.data and tempStack.peek() > temp:
        self.data.append(tempStack.pop())
      tempStack.append(temp)

    self.data = tempStack

if __name__ == '__main__':
  s = Stack()
  s.append(5)
  s.append(15)
  s.append(7)
  s.append(-1)
  s.append(0)
  print s
  print s.peek()
  # s.pop()
  print s
  s.sort()
  print s






