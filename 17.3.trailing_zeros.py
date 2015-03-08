# 2:27
def getZeros(n = None):
  if not n:
    return 0

  i, count = 5, 0
  while n // i > 0:
    count += n // i
    i *= 5

  return count


if __name__ == '__main__':
  print getZeros(101)
