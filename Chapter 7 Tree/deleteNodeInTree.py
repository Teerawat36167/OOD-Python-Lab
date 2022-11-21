class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def insert(self, val):  
        newData = Node(val)
        if self.root is None :
            self.root = newData
        else :
            cur = self.root
            while True :
                if cur.data > val :
                    if cur.left is None :
                        cur.left = newData
                        break
                    else :
                        cur = cur.left
                elif cur.data <= val :
                    if cur.right is None :
                        cur.right = newData
                        break
                    else :
                        cur = cur.right
        return self.root

    def delete(self, r, data):
        if r is None: 
            print("Error! Not Found DATA")
            return

        if self.root.left == None and self.root.right == None and self.root.data == data:
            self.root = None
        elif self.root.left == None and self.root.data == data:
            self.root = self.root.right
        elif self.root.right == None and self.root.data == data:
            self.root = self.root.left

        if r.data != data :
            if r.data > data :
                r.left = self.delete(r.left, data)
            elif r.data < data :
                r.right = self.delete(r.right, data) 
        elif r.data == data :
            if r.left == None :
                r = r.right
                return r
            elif r.right == None :
                r = r.left
                return r
            else:
                current = r.right
                while current.left != None :
                    current = current.left
                r.data = current.data 
                r.right = self.delete(r.right, current.data)

        return r
            
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


tree = BinarySearchTree()
data = input("Enter Input : ").split(",")

for i in data :
    inp = i.split(" ")
    if inp[0] == 'i' :
        tree.insert(int(inp[1]))
        print(f'insert {inp[1]}')
        printTree90(tree.root)
    elif inp[0] == 'd' :
        print(f'delete {inp[1]}')
        tree.delete(tree.root,int(inp[1]))
        printTree90(tree.root)