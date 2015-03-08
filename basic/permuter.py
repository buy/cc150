class Permuter:
  def __init__(self, string):
    self.flags = [False] * len(string)
    self.output = []
    self.string = string

  def permute(self):
    if len(self.output) is len(self.string):
      print ''.join(self.output)
      return None

    for i in range(len(self.string)):
      if self.flags[i]:
        continue

      self.output.append(self.string[i])
      self.flags[i] = True
      self.permute()
      self.output.pop()
      self.flags[i] = False


if __name__ == '__main__':
  p = Permuter('abc1')
  p.permute()
