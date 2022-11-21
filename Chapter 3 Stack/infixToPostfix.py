class Stack :

    def __init__(self,list = None) :
        if list == None :
            self.list = []
        else :
            self.list = list

    def isEmpty(self) :
        return len(self.list) == 0

    def push(self,data) :
        self.list.append(data)

    def pop(self) :
        return self.list.pop(-1)

    def size(self) :
        return len(self.list)

    def peek(self) :
        return self.list[-1]

    def __str__(self) :
        return "".join(self.list)

operator = {
    "(" : 0,
    ")" : 0,
    "-" : 1,
    "+" : 1,
    "*" : 3,
    "/" : 3,
    "^" : 4,
}

def infix2postfix(exp) :

    s = Stack()

    postfix = ""

    for i in range(len(exp)) :
        if exp[i] in "+-*/()^" :
            if s.isEmpty() :
                s.push(exp[i])
            else :
                stack = s.pop()
                if exp[i] == '(' :
                    s.push(stack)
                    s.push(exp[i])
                elif exp[i] == ')' :
                    s.push(stack)
                    top = s.pop()
                    while top != '(':
                        postfix += top
                        top = s.pop()
                elif operator[stack] >= operator[exp[i]] :
                    postfix += stack
                    while not s.isEmpty() :
                        subStack = s.pop()
                        if operator[subStack] >= operator[exp[i]] :
                            postfix += subStack
                        elif operator[subStack] < operator[exp[i]] :
                            s.push(subStack)
                            break
                    s.push(exp[i])
                elif operator[stack] < operator[exp[i]] :
                    s.push(stack)
                    s.push(exp[i])
        else :
            postfix += exp[i]
    while not s.isEmpty() :
        postfix += s.pop()
    return postfix


print(" ***Infix to Postfix***")

token = input("Enter Infix expression : ")

print("PostFix : ")

print(infix2postfix(token))