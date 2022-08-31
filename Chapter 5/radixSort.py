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

     def __getitem__(self,index) :
          cur = self.head
          for _ in range(index) :
               cur = cur.next
          return cur.value

     def isEmpty(self):
          return self.head == None

     def addHead(self, item):
          new = Node(item)
          if self.isEmpty() :
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
          if self.isEmpty() :
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

     def deQueue(self) :
          cur = self.head
          q = self.head.value
          if cur.next == None:
               self.head = None
          else:
               self.head = cur.next
          return q

     def pop(self):
          current = self.head
          # if pos == 0 :
          if current.next == None :
               self.head = None
               self.tail = None
          else :
               self.head = current.next
          # else :
          #      for _ in range(pos-1) :
          #           current = current.next
          #      current.next = current.next.next

def radix_sort(input) :
     L = LinkedList()
     for i in input :
          L.append(i)

     LL = LinkedList()
     for _ in range(10) :
          LL.append(LinkedList())

     round = 1
     # while 1 :
     for _ in range(10) :
          while not L.isEmpty() :
               num = L.deQueue()
               index_digit = get_digit(int(num),round)
               LL[index_digit].append(num)
          print("Round :",round)
          for j in range(0,10) :
               print(j,": ",end='')
               if LL[j].isEmpty() :
                    print("")
               else :
                    print(LL[j])
          for i in range (10) :
               while not LL[i].isEmpty() :
                    L.append(LL[i].deQueue())
          round += 1
          print("------------------------------------------------------------")

def get_digit(n, d):
     for _ in range(d-1):
          n //= 10
     return n % 10

input = input("Enter Input : ").split(" ")
print("------------------------------------------------------------")
x = radix_sort(input)