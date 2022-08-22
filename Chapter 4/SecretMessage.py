class Queue :
    def __init__(self,ls = None) :
        if ls == None :
            self.q = []
        else :
            self.q = list(ls)

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

def encodemsg(q1, q2) :
    count = q1.size()
    for i in range(count) :
        ascii = q2.deQueue()
        encode = ord(q1.deQueue()) + int(ascii)
        if 122 < encode or ( 97 > encode and encode > 90 ) :
            encode -= 26
        q1.enQueue(chr(encode))
        q2.enQueue(ascii)

    for j in range(q2.size()-(q1.size()%q2.size())) :
        temp = q2.deQueue()
        q2.enQueue(temp)
    
    print("Encode message is : " , q1)

def decodemsg(q1, q2) :
    count = q1.size()
    for i in range(count) :
        ascii = int(q2.deQueue())
        char = ord(q1.deQueue())
        # encode = ord(q1.deQueue()) - int(ascii)
        if chr(char).isupper() and char - 65 < ascii :
            q1.enQueue(chr(char+26-ascii))
        elif chr(char).islower() and char - 97 < ascii :
            q1.enQueue(chr(char+26-ascii))
        else :
            q1.enQueue(chr(char-ascii))
        q2.enQueue(ascii)
    print("Decode message is : " , q1)

string,number = input("Enter String and Code : ").split(",")

q1 = Queue(string.replace(" ",""))

q2 = Queue(number)

encodemsg(q1, q2)

decodemsg(q1, q2)