def hasRoute(node1, node2):
  if node1 is None or node2 is None:
    return False

  queue = [node1]

  while queue:
    temp = queue.pop(0)
    if temp:
      temp.state = 'visited'
      if temp is node2:
        return True
      else:
        for node in temp.adjacent:
          if node.state != 'visited':
            queue.append(node)

  return False


if __name__ == '__main__':
  node1 = None
  node2 = None
  print hasRoute(node1, node2)
