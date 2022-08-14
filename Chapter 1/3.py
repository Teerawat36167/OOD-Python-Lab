from ast import Num
from itertools import count


print("*** Election ***")
numOfVote = int(input("Enter a number of voter(s) : "))
num = input().split()

def most_frequent(List):
    return max(set(List), key = List.count)

for i in range(0, len(num)):
    num[i] = int(num[i])

for i in num:
    if  i <= 0 or i > 20 :
        num.remove(i)

if most_frequent(num) >= 1 and most_frequent(num) <= 20 :
    print(most_frequent(num))
else :
    print("*** No Candidate Wins ***")