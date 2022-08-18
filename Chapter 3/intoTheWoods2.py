class Stack:
    def __init__(self) :
        self.items = []

    def push(self,i) :
        self.items.append(i)

    def pop(self) :
        self.items.pop(-1)

    def isEmpty(self) :
        return len(self.items) == 0

    def size(self) :
        return len(self.items)

