def compressString(src):
  if type(src) is not type(''):
    return None 

  if len(src) is 0:
    return ''

  output = []
  currentChar = src[0]
  count = 0

  for char in src:
    if char is currentChar:
      count += 1
    else:
      output.extend([currentChar, str(count)])
      currentChar = char
      count = 1

  output.extend([currentChar, str(count)])

  if len(output) < len(src):
    return ''.join(output)
  else:
    return src


if __name__ == '__main__':
  src = 'aabbcccdddaaa111'
  print compressString(src)
