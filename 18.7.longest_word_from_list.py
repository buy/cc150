# 5:36
def findLongestWordInList(array = None):
  if not array:
    return ''

  stringMap = {}
  for s in array:
    stringMap[s] = True
  array.sort(key = lambda x: -len(x))

  for s in array:
    if isValidLongString(s, stringMap, True):
      return s

  return ''

def isValidLongString(s = None, stringMap = None, isSelf = True):
    if not s or not stringMap:
      return False

    if s in stringMap and not isSelf:
      return True

    for i in range(1, len(s)):
      left, right = s[:i], s[i:]

      if left in stringMap and stringMap[left] and isValidLongString(right, stringMap, False):
        return True

    stringMap[s] = False
    return False



if __name__ == '__main__':
  a = ['cat', 'banana', 'dog', 'nana', 'walk', 'walker', 'dogwalker']
  print findLongestWordInList(a)
