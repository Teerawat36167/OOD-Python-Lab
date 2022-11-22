def insert(index,arr):
    if index == len(arr):
        return
    print(f'insert {arr[index]}',end='')
    check(index,arr)
    print(f'{arr[:index+1]}',end='')
    if len(arr[index+1:]) != 0:
        print(f' {arr[index+1:]}',end='')
    print()
    insert(index+1,arr)

def check(index,arr):
    insertIndex = int()
    if index == 0:
        print(f' at index {insertIndex} : ',end='')
        return 0
    if arr[index] < arr[index-1]:
        insertIndex = index-1
        temp = arr[index]
        arr[index] = arr[index-1]
        arr[index-1] = temp
        return check(index-1,arr)
    insertIndex = index
    print(f' at index {insertIndex} : ',end='')
    return 

ls = [2,6,3,5,4,1]
insert(1,ls)
print(f'sorted \n{ls}')