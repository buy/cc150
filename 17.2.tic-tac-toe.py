# 12:17

def hasWon(board = None):
  if not board or not len(board):
    return False

  rowLength = len(board)
  colLength = len(board[0])

  # Check row
  for i in range(rowLength):
    col = 0
    if board[i][col] == -1:
      break

    while col < colLength - 1:
      if board[i][col] != board[i][col + 1]:
        break
      col += 1
    if col == colLength - 1:
      return str(board[i][0]) + ' won!'

  # Check col
  for i in range(colLength):
    row = 0
    if board[row][i] == -1:
      break

    while row < rowLength - 1:
      if board[row][i] != board[row + 1][i]:
        break
      row += 1

    if row == rowLength - 1:
      return str(board[0][i]) + ' won!'

  # Check diagonal bottom left to top right
  i = 0
  while i < rowLength - 1:
    if board[i][i] != board[i + 1][i + 1]:
      break

    i += 1

  if i == rowLength - 1:
    return str(board[0][0]) + ' won!'

  return False
  



if __name__ == '__main__':
  board = [
    [0, 1, 1],
    [1, 0, 0],
    [0, 1, 0]
  ]

  print hasWon(board)
