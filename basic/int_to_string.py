def intToString(number):
  if type(number) is not type(1):
    return 'INVALID INPUT - NaN'

  if number is 0:
    return '0'

  negFlag = False

  if number < 0:
    negFlag = True
    number = -number

  output = []
  while number:
    digit = number % 10
    output.append(digit)
    number = number // 10

  if negFlag:
    output.append('-')

  return ''.join([str(elem) for elem in output][::-1])


if __name__ == '__main__':
  print intToString(123)
  print intToString(0)
  print intToString(-0)
  print intToString(-991)
