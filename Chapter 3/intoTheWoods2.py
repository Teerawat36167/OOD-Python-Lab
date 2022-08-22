class Stack:
    def __init__(self) :
        self.items = []

    def push(self,i) :
        self.items.append(i)

    def pop(self) :
        return self.items.pop(-1)

    def top(self) :
        return self.items[-1]

    def isEmpty(self) :
        return len(self.items) == 0

    def size(self) :
        return len(self.items)

    def clear(self) :
        self.items = []

    def __str__(self) :
        return str(self.items)

input = input("Enter Input : ").split(",")

s = Stack()
s2 = Stack()

for i in range(len(input)) :
    if input[i][0] == 'A' :
        num = int(input[i].split(" ")[1])
        s.push(num)
        while not s2.isEmpty() and num >= int(s2.top()) :
            s2.pop()
        s2.push(num)
    elif input[i][0] == 'B' :
        print(s2.size())
    elif input[i][0] == 'S' :
        s2.clear()
        stack = []
        while not s.isEmpty() :
            height = int(s.pop())
            if height % 2 != 0 :
                height += 2
            else :
                height -= 1
            stack.append(str(height))
        stack.reverse()
        for j in stack :
            s.push(j)
            while not s2.isEmpty() and int(j) >= int(s2.top()) :
                s2.pop()
            s2.push(j)