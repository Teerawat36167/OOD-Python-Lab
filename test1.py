def combi(arr: list) -> list:
     if len(arr) == 0:
          return [[]]
     
     first = arr[0]
     restofArr = arr[1:]
     combsA = combi(restofArr)
     combsB = []

     for comb in combsA:
          c = [first] + comb
          combsB.append(c)
          
     return combsA + combsB

list = [1,2,3,4]
print(combi(list))