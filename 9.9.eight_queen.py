# 10:20

class EightQueens:
  def __init__(self):
    self.output = []

  def placeQueens(self, n = 8, row = 0, temp = None):
    if temp is None:
      temp = []

    # print n, row, temp

    if row == n:
      self.output.append(temp[:])
      return

    for i in range(n):
      if self.isValidPosition(row, i, temp):
        temp.append(i)
        self.placeQueens(n, row + 1, temp)
        temp.pop()

    return self.output

  def isValidPosition(self, row, col, temp):
    for i in range(row):
      if temp[i] == col:
        return False

      if abs(temp[i] - col) == row - i:
        return False

    return True


if __name__ == '__main__':
  eq = EightQueens()
  print len(eq.placeQueens(8))
