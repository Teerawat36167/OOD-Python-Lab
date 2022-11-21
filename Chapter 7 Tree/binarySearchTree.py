class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        newData = Node(data)
        if self.root is None :
            self.root = newData
        else :
            cur = self.root
            while True :
                if cur.data > data :
                    if cur.left is None :
                        cur.left = newData
                        break
                    else :
                        cur = cur.left
                elif cur.data <= data :
                    if cur.right is None :
                        cur.right = newData
                        break
                    else :
                        cur = cur.right
        return self.root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)