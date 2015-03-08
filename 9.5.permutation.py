# 9:15

class Permuter:
  def __init__(self, string):
    self.string = string
    self.flag = [False] * len(string)
    self.output = []

  def permute(self):
    if len(self.output) is len(self.string):
      print self.output
      return

    for i in range(len(self.string)):
      if not self.flag[i]:
        self.output.append(self.string[i])
        self.flag[i] = True
        self.permute()
        self.flag[i] = False
        self.output.pop()
  

if __name__ == '__main__':
  p = Permuter('abc1')
  p.permute()
