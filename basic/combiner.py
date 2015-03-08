class Combiner:
  def __init__(self, inputString):
    self.inputString = inputString
    self.output = []

  def combine(self, pos = 0):
    for i in range(pos, len(self.inputString)):
      self.output.append(self.inputString[i])
      print self.output
      if i != len(self.inputString) - 1:
        self.combine(i+1)
      self.output.pop()


if __name__ == '__main__':
  c = Combiner('abcde')
  c.combine()
