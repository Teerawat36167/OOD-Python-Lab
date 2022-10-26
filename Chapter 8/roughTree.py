# class Node:
#      def __init__(self, data):
#           self.data = data
#           self.left = None
#           self.right = None
     
#      def __str__(self):
#           return str(self.data)

# class BST:
#      def __init__(self):
#           self.root = None

#      def insert(self, cur, data):
#           if self.root is None:
#                self.root = Node(data)
#                return self.root
          
#           if cur.data == data:
#                return self.root
          
#           if cur.data < data:
#                if cur.right is not None:
#                     self.insert(cur.right, data)
#                else:
#                     cur.right = Node(data)
#           else:
#                if cur.left is not None:
#                     self.insert(cur.left, data)
#                else:
#                     cur.left = Node(data)
          
#           return self.root

#      def printTree(self, node, level = 0):
#           if node != None:
#                self.printTree(node.right, level + 1)
#                print('     ' * level, node)
#                self.printTree(node.left, level + 1)

#      def sumTree(self, root):
#           if root is None:
#                return 0
          
#           suml = self.sumTree(root.left)
#           sumr = self.sumTree(root.right)

#           return root.data + suml + sumr

# T = BST()
# root = None

# inp = input('Enter Input : ').split('/')
# n = int(inp[0])
# data = [int(i) for i in inp[1].split()]

# if (n//2)+1 != len(data) or n % 2 == 0 or n < 3:
#      print("Incorrect Input")
#      exit(0)

# treeQ = list()

# for n in data :
#      n = Node(n)
#      treeQ.append(n)

# while len(treeQ) > 1:
#      n1 = treeQ.pop(0)
#      n2 = treeQ.pop(0)
#      minData = min(n1.data, n2.data)
#      n1.data -= minData
#      n2.data -= minData

#      newNode = Node(minData)
#      newNode.left = n1
#      newNode.right = n2

#      if len(treeQ) % 2 == 0 and len(treeQ) > 1:
#           treeQ.append(newNode)
#      else:
#           treeQ.insert(0, newNode)

# root = treeQ[0]
# T.printTree(root)
# print(T.sumTree(root))

inp = input("Enter Input : ").split("/")
n, l, ans = int(inp[0]), [int(i) for i in inp[1].split()], 0

if n//2 + 1 == len(l):
     ll = [None]*(n+1)
     for i in range(n//2+1,n+1):
          ll[i] = l[i-(n//2+1)]
     for i in range(n,0,-1):
          if ll[i] == None:
               mn = min(ll[2*i],ll[2*i+1])
               ll[2*i] -= mn
               ll[2*i+1] -= mn
               ll[i] = mn
     for i in range(1,n+1):
          ans += int(ll[i])
     print(ans)
else:
     print("Incorrect Input")