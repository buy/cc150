# 8:51

def getSubset(inputSet, pos=0, tempOutput=[], output=[]):
  for i in range(pos, len(inputSet)):
    tempOutput.append(inputSet[i])
    output.append(set(tempOutput))
    getSubset(inputSet, i+1, tempOutput, output)
    tempOutput.pop()

  return output

def getSubsetIT(inputSet):
  output = [[]]
  for x in inputSet:
    for i in range(len(output)):
      print output[i], 'aaa'
      new = output[i][:]
      new.append(x)
      print new, 'new'
      output.append(new)
      print output, 'xxxx'

  return output

if __name__ == '__main__':
  inputSet = {1,2,3}
  inputSet.add(2)
  print getSubset(list(inputSet))
  print getSubsetIT(list(inputSet))

  b = [1,2,3,4,5,2,3]
