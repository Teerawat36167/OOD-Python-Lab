def hbd(age):
    base = None
    if age % 2 == 0 :
        base = age//2
        return "saimai is just 20, in base " + str(base) + "!"
    else :
        base = age//2
        return "saimai is just 21, in base " + str(base) + "!"

year = input("Enter year : ")

print(hbd(int(year)))