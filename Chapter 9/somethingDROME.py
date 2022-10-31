def metadrome(list):
    pass

def plaindrome(list):
    pass

def katadrome(list):
    pass

def nialpdrome(list):
    pass

def repdrome(list):
    pass

inp = [int(num) for num in input("Enter Input : ")]

if metadrome(inp):
    print("Metadrome")
elif plaindrome(inp):
    print("Plaindrome")
elif katadrome(inp):
    print("Katadrome")
elif nialpdrome(inp):
    print("Nialpdrome")
elif repdrome(inp):
    print("Repdrome")
else:
    print("Nondrome")