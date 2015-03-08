def addWithoutPlus(a, b):
  if b == 0:
    return a

  sumWithoutCarry = a ^ b
  carry = (a & b) << 1

  return addWithoutPlus(sumWithoutCarry, carry)


if __name__ == '__main__':
  a = 35
  b = 22

  print addWithoutPlus(a, b)
