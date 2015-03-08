# 1:30

def findChange(changesAvailable = None, amonut = 25):
  if changesAvailable is None:
    changesAvailable = [1, 5, 10, 25]

  if amonut == 0:
    return 1

  if amonut < 0 or not changesAvailable:
    return 0

  curChange = changesAvailable[-1]

  return findChange(changesAvailable[:-1][:], amonut) + findChange(changesAvailable[:], amonut - curChange)
  
  

def findMinChange(n = 0, map = {}):
  if n in map:
    return map[n]

  if n < 0:
    return float('inf')

  if n == 0:
    return 0

  map[n] = min(findMinChange(n-1), findMinChange(n-5), findMinChange(n-10), findMinChange(n-25)) + 1

  return map[n]

if __name__ == '__main__':
  print findChange([1, 5, 10, 25], 135)
  print findMinChange(135)
