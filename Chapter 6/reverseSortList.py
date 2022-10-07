def reverse_sort_list(l, i, j):
     n = len(l)
     if i < n and j >= 0:
          if int(l[j]) > int(l[j + 1]):
               temp = l[j + 1]
               l[j + 1] = l[j]
               l[j] = temp
          reverse_sort_list(l, i, j - 1)
     if j == 0:
          reverse_sort_list(l, i + 1, i)
     return l

def reverse_list(list,index) :
     tempList.append(int(list[index]))
     if index == 0 :
          return tempList
     else :
          return reverse_list(list,index-1)
listt= input("Enter your List : ").split(",")
tempList = []
l =reverse_sort_list(listt, 1, 0)
print(f'List after Sorted : {reverse_list(l,len(l)-1)}')