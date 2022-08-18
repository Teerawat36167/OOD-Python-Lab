class Stack():

    def __init__(self):
        self.ls = []

    def push(self,i):
        self.ls.append(i)

    def pop(self):
        return self.ls.pop(-1)

    def isEmpty(self):
        return len(self.ls) == 0

    def size(self):
        return len(self.ls)
    
    def __str__(self):
        return " ".join(self.ls)

def postFixeval(st):

    s = Stack()

    for i in range(len(st)) :
        if st[i] not in "+-*/" :
            s.push(st[i])
        else :
            first = float(s.pop())
            second = float(s.pop())
            if st[i] == '+' :
                s.push(first + second)
            elif st[i] == '-' :
                s.push(second - first)
            elif st[i] == '*' :
                s.push(first * second)
            elif st[i] == '/' :
                s.push(second / first)
    return s.pop()

print(" ***Postfix expression calcuation***")

token = list(input("Enter Postfix expression : ").split())



print("Answer : ",'{:.2f}'.format(postFixeval(token)))