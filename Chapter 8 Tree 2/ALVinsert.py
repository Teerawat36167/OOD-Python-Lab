class TreeNode(object): 
     def __init__(self, val): 
          self.val = val 
          self.left = None
          self.right = None
          self.height = 1

class AVL_Tree(object): 
     def __init__(self) :
          self.root = None

     def insert(self, node, data) :
          if not node:
               return TreeNode(data)
          elif data < node.val:
               node.left = self.insert(node.left, data)
          else:
               node.right = self.insert(node.right, data)
          # Update height ancestor node
          node.height = 1 + max(self.height(node.left),self.height(node.right))
          # Get balance factor
          balance = self.getBalance(node)
          # If the node is unbalanced,then try out the 4 cases
          # Case 1 Left Left
          if balance > 1 and data < node.left.val:
               print("Not Balance, Rebalance!")
               return self.rightRotate(node)
          # Case 2 Right Right
          if balance < -1 and data > node.right.val:
               print("Not Balance, Rebalance!")
               return self.leftRotate(node)
          # Case 3 Left Right
          if balance > 1 and data > node.left.val:
               print("Not Balance, Rebalance!")
               node.left = self.leftRotate(node.left)
               return self.rightRotate(node)
          # Case 4 Right Left
          if balance < -1 and data < node.right.val:
               print("Not Balance, Rebalance!")
               node.right = self.rightRotate(node.right)
               return self.leftRotate(node)
          return node

     def height(self, node) :
          if not node:
               return 0
          return node.height

     def leftRotate(self, z) :
          y = z.right
          T2 = y.left
          y.left = z
          z.right = T2
          z.height = 1 + max(self.height(z.left),self.height(z.right))
          y.height = 1 + max(self.height(y.left),self.height(y.right))
          return y

     def rightRotate(self, z) :
          y = z.left
          T3 = y.right
          y.right = z
          z.left = T3
          z.height = 1 + max(self.height(z.left),self.height(z.right))
          y.height = 1 + max(self.height(y.left),self.height(y.right))
          return y
     
     def getBalance(self, root):
          if not root:
               return 0
          return self.height(root.left) - self.height(root.right)

def printTree90(node, level = 0):
     if node != None:
          printTree90(node.right, level + 1)
          print('     ' * level, node.val)
          printTree90(node.left, level + 1)

myTree = AVL_Tree()
root = None

data = [int(i) for i in input('Enter Input : ').split()]
for e in data:
     print("insert :",e)
     root = myTree.insert(root, e)
     printTree90(root)
     print("===============")