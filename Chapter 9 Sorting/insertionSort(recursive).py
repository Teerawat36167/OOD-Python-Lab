def insertionSort(list,n):
    if n <= 1:
        return
    insertionSort(list,n-1)
    last = list[n-1]
    j = n-2

    while (j>=0 and list[j]>last):
        list[j+1] = list[j]
        j = j-1
    list[j+1]=last

    if len(list[n:]) == 0:
        print(f'insert {last} at index {j+1} : {list[:n]}\nsorted')
    else:
        print(f'insert {last} at index {j+1} : {list[:n]} {list[n:]}')
    return list

inp = [int(i) for i in input("Enter Input : ").split()]
print(insertionSort(inp,len(inp)))