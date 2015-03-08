def countPath(end=[0, 0], cache={}):
  if tuple(end) in cache:
    return cache[tuple(end)]

  if end[0] < 0 or end[1] < 0:
    return 0

  if end == [0, 1] or end == [1, 0]:
    return 1

  up = end[:]
  up[0] -= 1
  left = end[:]
  left[1] -= 1

  cache[tuple(end)] = countPath(left, cache) + countPath(up, cache)

  return cache[tuple(end)]

if __name__ == '__main__':
  print countPath([199, 159])
