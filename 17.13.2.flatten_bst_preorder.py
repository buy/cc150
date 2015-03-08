from basic import *

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 4:10

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if not root:
            return None
            
        left = self.flatten(root.left)
        right = self.flatten(root.right)
        root.left = None
        root.right = None
        
        if left:
            root.right = left
        if right:
            self.getTail(root).right = right
        
        return root
    
    def getTail(self, root):
        if not root:
            return None
        
        while root.right:
            root = root.right
        
        return root
        
if __name__ == '__main__':
  t = BinaryTree()
  root = Node(5)
  t.add(root)
  t.add(Node(2))
  t.add(Node(1))
  t.add(Node(3))
  t.add(Node(4))
  t.add(Node(7))
  t.add(Node(6))
  t.add(Node(8))
  t.preOrder(t.root)
  print '\n======='

  a = Solution()
  a.flatten(root)
  print a
  n = root
  while n:
    print n.data,
    n = n.right
