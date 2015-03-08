def reverseW(string):
  if type(string) is not type(''):
    return None

  return string[::-1], ' '.join(string.split()[::-1])

def reverseWAdv(string):
  if type(string) is not type(''):
    return None

  word = []
  output = []
  for char in string:
    if char != ' ':
      word.append(char)
    else:
      output.append(''.join(word))
      word = []

  if word:
    output.append(''.join(word))

  return ' '.join(output[::-1])

def reverseSAdv(string):
  if type(string) is not type(''):
    return None

  length = len(string)
  stringList = list(string)

  for i in range(length / 2):
    stringList[i], stringList[length-1-i] = stringList[length-1-i], stringList[i]

  return ''.join(stringList)

if __name__ == '__main__':
  print reverseW('Hello World!')
  print reverseWAdv('Hello World!')
  print reverseSAdv('Hello World!')
