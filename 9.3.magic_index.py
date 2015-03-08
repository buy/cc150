# 1:30
# 1:35 - 1:40
def getMagicIndex(inputArray = None):
  if not inputArray:
    return -1

  for i in range(len(inputArray)):
    if i is inputArray[i]:
      return i

  return -1

def getMagicIndexAdv(inputArray = None, low=0, high=None):
  if not inputArray or type(inputArray) is not type([]):
    return -1

  if high is None:
    high = len(inputArray) - 1

  while low <= high:
    mid = (low + high) / 2

    if inputArray[mid] == mid:
      return mid
    elif inputArray[mid] > mid:
      high = mid - 1
    else:
      low = mid + 1

  return -1

if __name__ == '__main__':
  inputArray = [-1, 0, 2, 5]
  # inputArray = [-1, 0, 1, 5]
  print getMagicIndex(inputArray)
  print getMagicIndexAdv(inputArray)
