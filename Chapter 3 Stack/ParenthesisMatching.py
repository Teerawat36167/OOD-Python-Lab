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

    def __str__(self):
        return "".join(self.items)

def parenMatching(str) :
    s = Stack()
    NotError = True
    print(str,end = " ")
    for i in range(len(str)) :
        if str[i] in "([{" :
            s.push(str[i])
        else :
            if str[i] in ")]}" and not s.isEmpty() :
                pop = s.pop()
                if (pop == "(" and str[i] == ")") or (pop == "[" and str[i] == "]") or (pop == "{" and str[i] == "}"):
                    continue
                else:
                    print("Unmatch open-close") #Unmatch open-close
                    NotError = False
                    break
            elif str[i] not in ")]}" :
                continue
            else :
                print("close paren excess") #close paren excess
                NotError = False
                break
    if s.size() > 0 and NotError :
        print(f'open paren excess   {s.size()} : {s}') #open paren excess
    if s.size() == 0 and NotError:
        print("MATCH")

str = input("Enter expresion : ")

parenMatching(str)