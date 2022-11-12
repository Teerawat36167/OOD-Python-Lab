def combination(arr):
    def findSum(arr, n):
        if n == 0:
            return [[]]
        list = []
        for i in range(len(arr)):
            first = [arr[i]]
            remFirst = arr[i + 1 :]
            for j in findSum(remFirst, n - 1):
                list.append(sortList(first + j))
        return sortList(list)

    res = []
    for i in range(1, len(arr) + 1):
        res.extend(findSum(arr, i))
    return res

def sortList(list):
    for i in range(len(list)-1):
        for j in range(i+1,len(list)):
            if list[i] > list[j] :
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    return list

inp = input("Enter Input : ").split('/')
ans = int(inp[0])
inp = [int(i) for i in inp[1].split()]
subList = combination(inp)
subSet = []

for i in subList:
    if sum(i) == ans:
        subSet.append(i)

if len(subSet) != 0:
    for i in subSet:
        print(i)
else:
    print("No Subset")