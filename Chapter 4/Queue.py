class Queue :
    def __init__(self) :
        self.q=[]

    def enQueue(self,i) :
        self.q.append(i)

    def deQueue(self) :
        return self.q.pop(0)

    def isEmpty(self) :
        return len(self.q) == 0
    
    def isFull(self) :
        pass

    def size(self) :
        return len(self.q)