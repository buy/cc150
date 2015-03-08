#3:46

def hasElement(matrix = None, target = None):
  if not matrix or not target:
    return [-1, -1]

  row, col = 0, len(matrix) - 1
  while row < len(matrix) and col >= 0:
    if matrix[row][col] == target:
      return [row, col]
    elif matrix[row][col] > target:
      col -= 1
    else:
      row += 1

  return [-1, -1]

if __name__ == '__main__':
  matrix = [
    [15, 20, 40, 85],
    [20, 35, 80, 95],
    [30, 55, 95,105],
    [40, 80,100, 120]
  ]
  target = 55

  print hasElement(matrix, target)
