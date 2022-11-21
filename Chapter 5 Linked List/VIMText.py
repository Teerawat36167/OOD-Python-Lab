class Node:
     def __init__(self, value):
          self.value = value
          self.next = None
          self.previous = None

class LinkedList :

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

     def isEmpty(self):
          return self.head == None

     def addHead(self, item):
          new = Node(item)
          if L.isEmpty() :
               self.head = new
               self.tail = new
          else :
               current = self.head
               new.next = self.head
               current.previous = new
               self.head = new
               while current.next != None :
                    current = current.next
               self.tail = current

     def append(self, item):
          new = Node(item)
          if self.isEmpty() :
               self.head = new
               self.tail = new
          else :
               current = self.head
               while current.next != None :
                    current = current.next
               current.next = new
               new.previous = self.tail
               self.tail = new

     def insert(self, pos, item):
          new = Node(item)
          if L.isEmpty() :
               self.head = new
               self.tail = new
          else :
               current = self.head
               if pos < 0 :
                    self.addHead(new.value)
                    return
               else :
                    for _ in range(pos) :
                         current = current.next
               new.next = current.next
               new.previous = current
               current.next = new
               current = new
               if current.next != None :
                    current = current.next
                    current.previous = new
               while current.next != None :
                    current = current.next
               self.tail = current

     def index(self, item):
          n = 0
          if self.isEmpty() :
               return -1
          else :
               current = self.head
               while current :
                    if str(current.value) == str(item) :
                         return n
                    else :
                         current = current.next
                         n += 1
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
               if current.next == None :
                    self.head = None
                    self.tail = None
               else :
                    self.head = current.next
          else :
               for _ in range(pos-1) :
                    current = current.next
               current.next = current.next.next

L = LinkedList()

input = input("Enter Input : ").split(",")

cursor = "|"
L.append(cursor)

for i in range(len(input)) :
     if len(input[i]) > 1 :
          command, word = input[i].split(" ")
     else :
          command = input[i]
     if command == "I" :
          L.insert(L.index(cursor) - 1,word)
     elif command == "L" :
          posCursor = L.index(cursor)
          if posCursor != 0 :
               L.pop(posCursor)
               L.insert(posCursor - 2,cursor)
          else :
               continue
     elif command == "R" :
          posCursor = L.index(cursor)
          if posCursor != L.size() - 1 :
               L.pop(posCursor)
               L.insert(posCursor,cursor)
          else :
               continue
     elif command == "B" :
          posCursor = L.index(cursor)
          if posCursor != 0 :
               L.pop(posCursor - 1)
          else :
               continue
     elif command == "D" :
          posCursor = L.index(cursor)
          if posCursor != L.size() - 1 :
               L.pop(posCursor + 1)
          else :
               continue
print(L)