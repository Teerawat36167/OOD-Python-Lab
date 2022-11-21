class Queue :
    def __init__(self) :
        self.q=[]

    def enQueue(self,i) :
        self.q.append(i)

    def deQueue(self) :
        return self.q.pop(0)

    def isEmpty(self) :
        return len(self.q) == 0

    def size(self) :
        return len(self.q)

    def __str__(self) :
        return ", ".join(self.q)

input = input("Enter Input : ").split(",")

q = Queue()

dequeue = Queue()

for i in range(len(input)) :
    if input[i][0] == 'E' :
        q.enQueue(input[i][-1])
        print(q)
    elif input[i][0] == 'D' and not q.isEmpty():
        pop = q.deQueue()
        print(pop + " <- ",end='')
        if q.isEmpty() :
            print("Empty")
        else :
            print(q)
        dequeue.enQueue(pop)
    else :
        print("Empty")

if not dequeue.isEmpty() :
    print(dequeue , ":" ,end = '')
else :
    print("Empty :" ,end = '')

if q.isEmpty() :
    print(" Empty")
else :
    print("" , q)