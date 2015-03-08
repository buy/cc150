# 10:03

def selectionSort(array = None):
  if array is None:
    return None

  for i in range(len(array)):
    for j in range(i+1, len(array)):
      if a[i] > a[j]:
        a[i] , a[j] = a[j], a[i]


if __name__ == '__main__':
  a = [3,2,4,{'b':'a'},{'b':'b'},0,8,5,6,7,9]
  print a
  selectionSort(a)
  print a
