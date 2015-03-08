def binarySearch(inputArray, target):
  if type(inputArray) is not type([]):
    return -1

  low = 0
  high = len(inputArray) - 1

  while low <= high:
    mid = (low + high) / 2
    if inputArray[mid] < target:
      low = mid + 1
    elif inputArray[mid] > target:
      high = mid - 1
    else:
      return mid

  return -1

if __name__ == '__main__':
  a = [3, 4, 5, 7, 8]
  print binarySearch(a, 4)
