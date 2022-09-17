listPerket = []

def perket(index, n, b, s):
     if(index == len(inp)):
          if(n != 0):
               sum = abs(b-s)
               listPerket.append(sum)
          else :
               return

     inp1, inp2 = inp[index].split(" ") 
     sumS = s * int(inp1)
     sumB = b + int(inp2)
     
     perket(index + 1, n, b, s)
     perket(index + 1, n + 1, sumB, sumS)

inp = input("Enter Input : ").split(",")

perket(0, 0, 0, 1)
print(min(listPerket))
