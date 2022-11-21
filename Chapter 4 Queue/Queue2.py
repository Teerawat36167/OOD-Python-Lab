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
        return str(self.q)

input = list(input("Enter people : "))

qInput = Queue()
q1 = Queue()
q2 = Queue()

for i in range(len(input)) :
    qInput.enQueue(input[i])

q1count,q2count = 0,0

for i in range(len(input)) :
    if q1count == 3 : 
        q1count = 0
        q1.deQueue()
    if q2count == 2 : 
        q2count = 0
        q2.deQueue()
    if q1.size() < 5 :
        q1.enQueue(input[i])
        qInput.deQueue()
    else :
        if q2.size() < 5 :
            q2.enQueue(input[i])
            qInput.deQueue()
    if not q1.isEmpty() : q1count += 1
    if not q2.isEmpty() : q2count += 1
    print(i+1,qInput,q1,q2)