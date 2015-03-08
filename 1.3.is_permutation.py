def isPermutation(string1, string2):
  return sorted(string1) == sorted(string2)

if __name__ == '__main__':
  string1 = 'abcd   '
  string2 = 'cabd'
  print isPermutation(string1, string2)
