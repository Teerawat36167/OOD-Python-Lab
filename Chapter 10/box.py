def minWeight(items,box,min):
     count = 0
     weight = 0
     for item in items:
          if weight + item <= min:
               weight += item
          else:
               count += 1
               weight = item
     if count + 1 == box:
          return min
     return minWeight(items,box,min+1)

inp = input("Enter Input : ").split("/")
items = [int(i) for i in inp[0].split()]
numOfBox = int(inp[1])
print(f'Minimum weigth for {numOfBox} box(es) = {minWeight(items,numOfBox,max(items))}')