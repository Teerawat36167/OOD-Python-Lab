def bubbleSort(list, i, j):
     if i == 0:
          return
     if j < i :
          if list[j] > list[j+1]:
               temp = list[j]
               list[j] = list[j+1]
               list[j+1] = temp
          bubbleSort(list, i, j+1)
     else :
          bubbleSort(list, i-1, 0)

inp = [int(i) for i in input("Enter Input : ").split()]
bubbleSort(inp, len(inp)-1, 0)
print(inp)