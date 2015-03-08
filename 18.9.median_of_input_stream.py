import heapq

class MedianFinder:
  def __init__(self):
    self.maxHeap = []
    self.minHeap = []

  def addNumber(self, num):
    if len(self.maxHeap) == len(self.minHeap):
      if self.minHeap and num > self.minHeap[0]:
        heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        heapq.heappush(self.minHeap, num)
      else:
        heapq.heappush(self.maxHeap, -num)
    else:
      if num < -self.maxHeap[0]:
        heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        heapq.heappush(self.maxHeap, -num)
      else:
        heapq.heappush(self.minHeap, num)
    

  def getMedian(self):
    print self.maxHeap, self.minHeap
    if not self.maxHeap:
      return 0

    if len(self.maxHeap) is len(self.minHeap):
      return (-heapq.heappop(self.maxHeap) + heapq.heappop(self.minHeap)) / 2
    else:
      return -heapq.heappop(self.maxHeap)


if __name__ == '__main__':
  stream = [1,2,3,4,5,6,7,8,9,10,-11]
  m = MedianFinder()
  for n in stream:
    m.addNumber(n)

  print m.getMedian()
