def firstChar(string):
  if type(string) is not type(''):
    return None

  usedChar = {}
  for char in string:
    if char not in usedChar:
      usedChar[char] = False
    else:
      usedChar[char] = True

  for char in string:
    if not usedChar[char]:
      return char

if __name__ == '__main__':
  print firstChar('aaaxaaax')
  print firstChar('aabbasf')
  print firstChar('bbbaaacccdd')
  print firstChar('ccbbaad')
  print firstChar('abcdef')
