# 11:11
def swap(a = None, b = None):
  if a is None or b is None:
    return None

  a = a^b
  b = a^b
  a = a^b

  return a, b


if __name__ == '__main__':
  a = 4
  b = 123
  print a, b
  a, b = swap(a, b)
  print a, b
