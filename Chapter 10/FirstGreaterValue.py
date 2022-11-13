inp = input('Enter Input : ').split('/')
left = sorted(list(map(int,inp[0].split())))
right = list(map(int,inp[1].split()))

for i in right:
     check = False
     for j in left:
          if i < j:
               print(j)
               check = True
               break
     if not check:
          print("No First Greater Value")