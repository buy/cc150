# 11:36
def reorder(array = None):
  if not array:
    return []

  isLessEqual = True

  for i in range(len(array) - 1):
    if (isLessEqual and array[i] > array[i + 1]) or (not isLessEqual and array[i] < array[i + 1]):
      array[i], array[i + 1] = array[i + 1], array[i]
    isLessEqual = not isLessEqual


if __name__ == '__main__':
  a = [1,2,3,4,5,6,7,8,9]
  print a
  reorder(a)
  print a
