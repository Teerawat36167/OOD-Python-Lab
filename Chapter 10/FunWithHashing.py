class Data:
     def __init__(self, key, value):
          self.key = key
          self.value = value

     def __str__(self):
          return "({0}, {1})".format(self.key, self.value)

class hash:
     def __init__(self,size,maxCol):
          self.table = [None]*size
          self.size = size
          self.maxCol = maxCol

     def insert(self,key,data):
          if self.isfull() :
               print("This table is full !!!!!!")
               exit(0)
          else:
               index = 0
               for i in key:
                    index += i
               index %= self.size

               if self.table[index] == None:
                    self.table[index] = Data(key,data)
               else:
                    col = 0
                    newIndex = index
                    print(f'collision number {col+1} at {index}')

                    #Not Finish

     def isfull(self):
          return None not in self.table

print(" ***** Fun with hashing *****")
inp = input("Enter Input : ").split('/')
size, maxCol = inp[0].split()
H = hash(int(size),int(maxCol))
data = inp[1].split(",")

for i in data:
     H.insert(i.split()[0],i.split()[1])