# 4:15
def getMaxProfit(stocks = None):
  if not stocks or len(stocks) is 1:
    return 0

  low, diff = stocks[0], 0

  for i in range(1, len(stocks)):
    if stocks[i] < low:
      low = stocks[i]

    if diff < stocks[i] - low:
      diff = stocks[i] - low

  return diff

if __name__ == '__main__':
  stocks = [9,8,7,6,5,4,98,3,99]
  print getMaxProfit(stocks)
