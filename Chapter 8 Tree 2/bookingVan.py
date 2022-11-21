class van:
    def __init__(self,num,time):
        self.num = int(num)
        self.time = int(time)
    
    def __lt__(self,o):
        if self.time == o.time:
            return self.num < o.num
        return self.time < o.time

inp = input("Enter Input : ").split("/")
n =  int(inp[0])
booking = [int(i) for i in inp[1].split()]
q = []

for i in range(n):
    q.append(van(i+1,0))

for i in range(len(booking)):
    firstVan = q.pop(0)
    print(f'Customer {i+1} Booking Van {firstVan.num} | {booking[i]} day(s)')
    q.append(van(firstVan.num,int(booking[i])+firstVan.time))
    q.sort()