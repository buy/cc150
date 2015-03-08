def hasAllUniqueChars(src):
  if type(src) is not type('123'):
    raise Exception('invalid input')

  charMap = {}
  for char in src:
    if char in charMap:
      return False
    else:
      charMap[char] = int('1', 2)

  return True

def hasAllUniqueCharsNoDS(src):
  pass

if __name__ == '__main__':
  print hasAllUniqueChars('abc1n2')
