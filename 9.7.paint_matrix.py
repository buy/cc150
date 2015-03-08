# 1:10

def paint(screen, point, newColor, oldColor=None):
  if not screen or not point or not newColor or not oldColor:
    return None

  if y < 0 or y >= len(screen) or x < 0 or x > len(screen[0]):
    return None

  if oldColor is None:
    oldColor = point.color

  if point.color == oldColor:
    point.color = newColor
    paint(point[y-1][x], newColor, oldColor)
    paint(point[y+1][x], newColor, oldColor)
    paint(point[y][x-1], newColor, oldColor)
    paint(point[y][x+1], newColor, oldColor)


if __name__ == '__main__':
  screen = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
  ]

  point = screen[1][2]
  newColor = 9
  paint(screen, point, newColor)
