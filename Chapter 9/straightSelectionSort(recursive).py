def maxIndex(list, i, j):
     if i == j:
          return i
     k = maxIndex(list, i + 1, j)
     return (k if list[i] < list[k] else i)

def straightSelectionSort(list, n):
     if n == 0:
          return
     k = maxIndex(list, 0, n)
     if k != n :
          temp = list[k]
          list[k] = list[n]
          list[n] = temp
          print(f'swap {list[k]} <-> {list[n]} : {list}')
     straightSelectionSort(list, n-1)

inp = [int(i) for i in input("Enter Input : ").split()]

straightSelectionSort(inp, len(inp)-1)

print(inp)