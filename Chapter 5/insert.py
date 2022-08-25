class Node:
    def __init__(self, data, next = None):
        self.data = data
        if next is None :
            self.next = None
        else :
            self.next = next

class LinkedList :
    def __init__(self) :
        self.head = None

    def append(self, data) :
        p = Node(data)
        if self.head == None :
            self.head = p
        else :
            t = self.head
            while t.next != None :
                t = t.next
            t.next = p

    def insert(self, index, data) :
        p = Node(data)
        if int(index) == 0 :
            p.next = self.head
            self.head = p
            print("index = 0 and data =",data)
        elif int(index) == self.size() :
            q = self.head
            while q.next != None :
                q = q.next
            q.next = p
            print("index = " + str(index).strip() + " and data = " + str(data))
        elif int(index) < 0 or int(index) > self.size():
            print("Data cannot be added")
        else :
            q = self.head
            for _ in range(int(index)-1) :
                if q.next == None :
                    print("Data cannot be added")
                    return
                else :
                    q = q.next
            p.next = q.next
            q.next = p
            print("index = " + str(index).strip() + " and data = " + str(data))

    def isEmpty(self) :
        return self.head == None

    def __str__(self) :
        output = "link list : "
        if self.isEmpty() :
            return "List is empty"
        p = self.head
        while p != None :
            output += str(p.data)
            if p.next != None :
                output += '->'
            p=p.next
        return output

    def size(self) :
        current = self.head
        n = 0
        while current :
            current = current.next
            n += 1
        return n

link = LinkedList()

input = input("Enter Input : ").split(",")

createLL = input[0].split(" ")

if createLL[0] == '':
    print("List is empty")
else :
    for i in range(len(createLL)) :
        link.append(createLL[i])
    print(link)

for i in range(len(input)-1) :
    index, data = input[i+1].split(":")
    link.insert(index, data)
    print(link)