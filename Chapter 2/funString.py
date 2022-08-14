class funString():

    def __init__(self,string = ""):
        self.string = string

    def __str__(self):
        return self.string

    def size(self) :
        return len(self.string)

    def changeSize(self):
        tempStr = ""
        for i in range(len(self.string)) :
            if self.string[i].isupper() :
                tempStr += self.string[i].lower()
            else :
                tempStr += self.string[i].upper()
        return tempStr

    def reverse(self):
        return self.string[::-1]

    def deleteSame(self):
        tempStr = ""
        for i in range(len(self.string)) :
            if not self.string[i] in tempStr :
                tempStr += self.string[i]
        return tempStr

str1,str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :  print(res.size())

elif str2 == "2":  print(res.changeSize())

elif str2 == "3" : print(res.reverse())

elif str2 == "4" : print(res.deleteSame())