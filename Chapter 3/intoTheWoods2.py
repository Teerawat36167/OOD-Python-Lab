class Stack:
    def __init__(self) :
        self.items = []

    def push(self,i) :
        self.items.append(i)

    def pop(self) :
        return self.items.pop(-1)

    def isEmpty(self) :
        return len(self.items) == 0

    def size(self) :
        return len(self.items)

input = input("Enter Input : ").split(",")

s = Stack()

for i in range(len(input)) :
    if input[i][0] == 'A' :
        s.push(input[i][-1])
    elif input[i][0] == 'B' :
        # turn around
    elif input[i][0] == 'S' :
        #