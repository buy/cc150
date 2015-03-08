def reverseString(src):
  return ' '.join(src.split()[::-1])

def reverseStringAdv(src):
  srcList = list(src)

  for i in range(len(src) / 2):
    srcList[i], srcList[len(src)-1-i] = srcList[len(src)-1-i], srcList[i]

  return ''.join(srcList)

if __name__ == '__main__':
  src = 'hello world gorupon!'
  print reverseString(src)
  print reverseStringAdv(src)
