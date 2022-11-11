def combination(arr):
    def findSum(arr, n):
        if n == 0:
            return [[]]
        list = []
        for i in range(len(arr)):
            start = arr[i]
            rem = arr[i + 1 :]
            for j in findSum(rem, n - 1):
                print([start])
                print(j)
                list.append(sortList([start] + j))
        return sortList(list)

    res = list()
    for i in range(1, len(arr) + 1):
        res.append(findSum(arr, i))
    return res

def sortList(list):
    for i in range(len(list)-1):
        for j in range(i+1,len(list)):
            if int(list[i]) > int(list[j]) :
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    return list

inp = input("Enter Input : ").split('/')
ans = int(inp[0])
inp = [int(i) for i in inp[1].split()]
subList = combination(inp)
subSet = []
print(subList)