class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        new = Node(item)
        current = self.head
        while current.next != None :
            current = current.next
        current.next = new

    def addHead(self, item):
        new = Node(item)
        new.next = self.head
        self.head = new

    def insert(self, pos, item):
        new = Node(item)
        current = self.head
        for _ in range(pos-1) :
            if current.next == None :
                print("Data cannot be added")
                return
            else :
                current = current.next
        new.next = current.next
        current.next = new

    def search(self, item):
        current = self.head
        while current :
            if current == item :
                return "FOUND"
            else :
                current = current.next
        return "NOT FOUND"

    def index(self, item):
        current = self.head
        n = 0
        while current :
            if current == item :
                return n
            else :
                current = current.next
        return -1

    def size(self):
        current = self.head
        n = 0
        while current :
            current = current.next
            n += 1
        return n

    def pop(self, pos):
        current = self.head
        if pos == 0 :
            current = current.next
        elif pos == self.size() :
            while current.next.next != None :
                current = current.next
            current.next = current.next.next
        else :
            for _ in range(pos-2) :
                current = current.next
            current.next = current.next.next

l1 = LinkedList()
l2 = LinkedList()