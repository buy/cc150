def waysToClimb(steps, climb):
  if steps in climb:
    return climb[steps]
  elif steps < 0:
    return 0
  elif steps is 0:
    return 1

  climb[steps] = waysToClimb(steps-1, climb) + waysToClimb(steps-2, climb) + waysToClimb(steps-3, climb)
  return climb[steps]

if __name__ == '__main__':
  print waysToClimb(23, {})
