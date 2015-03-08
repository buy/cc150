# 9:50
def insertionSort(array = None):
  if array is None:
    return None

  for i in range(1, len(array)):
    var = array[i]
    j = i - 1
    while j >= 0 and array[j] > var:
      array[j+1] = array[j]
      j -= 1

    array[j+1] = var


if __name__ == '__main__':
  a = [3,2,4,{'b':'a'},{'b':'b'},0,8,5,6,7,9]
  print a
  insertionSort(a)
  print a
