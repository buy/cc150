# 12:16
def sortMiddleArray(a = None):
  if not a:
    return []

  middleStart, middleTail = 0, 0
  for i in range(1, len(a)):
    if a[i - 1] > a[i]:
      middleStart = i
      break

  for i in range(len(a) - 2, -1, -1):
    if a[i - 1] > a[i]:
      middleTail = i
      break

  print middleStart, middleTail

  for i in range(middleStart - 1, -1, -1):
    if a[i] < min(a[middleStart: middleTail]):
      middleStart = i + 1
      break

  for i in range(middleTail, len(a)):
    if a[i] > max(a[middleStart: middleTail]):
      middleTail = i - 1
      break

  return middleStart, middleTail


if __name__ == '__main__':
  a = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
  print a
  print sortMiddleArray(a)
  print a
