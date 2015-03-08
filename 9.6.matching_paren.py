# 12:20

class ParenGenerator:
  def __init__(self, n):
    self.openCount = self.closeCount = n
    self.output = []

  def generateParen(self, openCount = 0, closeCount = 0):
    if openCount > self.openCount or closeCount > openCount:
      return None

    if openCount + closeCount == self.openCount + self.closeCount:
      print ''.join(self.output)
      return None

    if openCount < self.openCount:
      self.output.append('(')
      openCount += 1
      self.generateParen(openCount, closeCount)
      self.output.pop()
      openCount -= 1

    if openCount > closeCount and closeCount < self.closeCount:
      self.output.append(')')
      closeCount += 1
      self.generateParen(openCount, closeCount)
      self.output.pop()
      closeCount -= 1
    
def generateParenthesis(n, openCount = 0, closeCount = 0, output = []):
        if openCount > n or closeCount > openCount:
            return None
    
        if openCount + closeCount == 2 * n:
            print ''.join(output)
            return None
    
        if openCount < n:
            output.append('(')
            openCount += 1
            generateParenthesis(n, openCount, closeCount, output)
            output.pop()
            openCount -= 1
    
        if openCount > closeCount and closeCount < n:
            output.append(')')
            closeCount += 1
            generateParenthesis(n, openCount, closeCount, output)
            output.pop()
            closeCount -= 1
if __name__ == '__main__':
  # p = ParenGenerator(1)
  # p.generateParen()
  generateParenthesis(2)
