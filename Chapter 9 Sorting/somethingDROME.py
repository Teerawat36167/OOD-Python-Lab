def metadrome(list):
    for i in range(1,len(list)):
        if list[i-1] > list[i] or list[i-1] == list[i]:
            return False
    return True

def plaindrome(list):
    repeat, ascending = False, True
    for i in range(1,len(list)):
        if list[i-1] > list[i]:
            ascending = False
        if list[i-1] == list[i]:
            repeat = True
    return ascending and repeat

def katadrome(list):
    for i in range(1, len(list)):
        if list[i-1] < list[i] or list[i-1] == list[i]:
            return False
    return True

def nialpdrome(list):
    repeat, descending = False, True
    for i in range(1, len(list)):
        if list[i-1] < list[i]:
            descending = False
        if list[i-1] == list[i]:
            repeat = True
    return repeat and descending

def repdrome(list):
    for i in range(1,len(list)):
        if list[i-1] != list[i]:
            return False
    return True

inp = [int(num) for num in input("Enter Input : ")]

if metadrome(inp):
    print("Metadrome")
elif repdrome(inp):
    print("Repdrome")
elif plaindrome(inp):
    print("Plaindrome")
elif katadrome(inp):
    print("Katadrome")
elif nialpdrome(inp):
    print("Nialpdrome")
else:
    print("Nondrome")