# 10:17
def mergeSort(array = None):
  if array is None:
    return None

  if len(array) is 1:
    return array

  return merge(mergeSort(array[:len(array)/2]), mergeSort(array[len(array)/2:]))

def merge(arrayA, arrayB):
  i = j = 0
  a = len(arrayA)
  b = len(arrayB)
  result = []

  while i < a and j < b:
    if arrayA[i] < arrayB[j]:
      result.append(arrayA[i])
      i += 1
    else:
      result.append(arrayB[j])
      j += 1

  if i < a:
    result.extend(arrayA[i:])
  if j < b:
    result.extend(arrayB[j:])

  return result



if __name__ == '__main__':
  a = [3,2,4,{'b':'a'},{'b':'b'},0,8,5,6,7,9]
  print a
  print mergeSort(a)
