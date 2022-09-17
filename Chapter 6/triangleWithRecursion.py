def staircase(k,n):
     if (abs(k)-1) == n:
          if k > 0 :
               return "_" * (k-n-1) + "#" * (n+1)
          else :
               return "_" * n + "#" * (abs(k)-n)

     if k > 0 :
          return "_" * (k-n-1) + "#" * (n+1) + "\n" + str(staircase(k,n+1))
     elif k < 0 :
          return "_" * n + "#" * (abs(k)-n) + "\n" + str(staircase(k,n+1))
     elif k == 0 :
          return "Not Draw!"

print(staircase(int(input("Enter Input : ")),0))