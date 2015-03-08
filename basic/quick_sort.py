# 9:16
def quickSort(array = None, low = 0, high = None):
  if array is None:
    return None

  if high is None:
    high = len(array) - 1

  if low > high:
    return None

  s, i, j = array[low], low, high

  while i < j:
    while i < j and s <= array[j]:
      j -= 1
    if i < j:
      array[i], array[j] = array[j], array[i]
      i += 1

    while i < j and s >= array[i]:
      i += 1
    if i < j:
      array[i], array[j] = array[j], array[i]
      j -= 1

  quickSort(array, low, i - 1)
  quickSort(array, i + 1, high)


if __name__ == '__main__':
  a = [3,2,4,{'b':'a'},{'b':'b'},0,8,5,7,6,9]
  print a
  quickSort(a)
  print a
