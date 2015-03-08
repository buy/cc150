def string_to_int(string):
  if type(string) is not type('') or len(string) < 1:
    return None

  negFlag = False
  pos = 0
  output = 0

  if string[0] == '-':
    negFlag = True
    pos = 1

  for i in range(pos, len(string)):
    output = output*10 + int(string[i])

  if negFlag:
    output = -output

  return output

if __name__ == '__main__':
  print string_to_int('123')
  print string_to_int('-123')
  print string_to_int('-')
  print string_to_int('0')
  print string_to_int('-099')
