# 1:03

def findMaxSumSeq(a = None):
  if not a:
    return []

  curMax = totalMax = 0

  for i in a:
    curMax += i
    if totalMax < curMax:
      totalMax = curMax
    elif curMax < 0:
      curMax = 0

  return totalMax

if __name__ == '__main__':
  seq = [2, -8, 3, -2, 4, -10]
  print findMaxSumSeq(seq)
