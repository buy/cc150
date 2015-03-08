def rand7():
  while True:
    num = 5 * rand5() + rand5()
    if num > 21:
      return num % 7
