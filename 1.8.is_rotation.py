def isSubstring(string1, string2):
  return string1 in string2

def isRotation(string1, string2):
  if type('') is not type(string1) or type('') is not type(string2):
    raise Exception('Not Strings!')

  if len(string1) is not len(string2):
    return False
  else:
    return isSubstring(string1, string1 + string2)


if __name__ == '__main__':
  print isRotation('abc', 'bca')
