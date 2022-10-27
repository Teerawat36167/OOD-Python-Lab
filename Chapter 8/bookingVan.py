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
        if self.root == None:
            self.root = Node(data)
        elif self.root != None:
            p = self.root
            found = False
            while not found:
                if p.left == None:
                    p.left = Node(data)
                    found = True
                elif p.right == None:
                    p.right = Node(data)
                    found = True
                elif p.left.left != None and p.left.right != None:
                    p = p.right
                else:
                    p = p.left

k,list = input("Enter Input : ").split('/')
list = [int(i) for i in list.split()]
print(list)