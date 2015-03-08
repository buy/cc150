# 4:42

def getMaxProfit(stocks = None):
  if not stocks or len(stocks) is 1:
    return 0

  profit = 0
  price = stocks[0]
  for i in range(1, len(stocks)):
    diff = stocks[i] - stocks[i-1]
    if diff > 0:
      profit += diff

  return profit

if __name__ == '__main__':
  stocks = [100, 180, 260, 310, 40, 535, 695]
  print getMaxProfit(stocks)
