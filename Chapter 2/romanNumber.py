class translator:

    def deciToRoman(self, num):
        self.num = num
        roman = ""
        while self.num > 0 :
            if self.num >= 1000 :
                roman = roman + "M"
                self.num -= 1000
            elif self.num >= 900 :
                roman = roman + "CM"
                self.num -= 900
            elif self.num >= 500 :
                roman = roman + "D"
                self.num -= 500
            elif self.num >= 400 :
                roman = roman + "CD"
                self.num -= 400
            elif self.num >= 100 :
                roman = roman + "C"
                self.num -= 100
            elif self.num >= 90 :
                roman = roman + "XC"
                self.num -= 90
            elif self.num >= 50 :
                roman = roman + "L"
                self.num -= 50
            elif self.num >= 40 :
                roman = roman + "XL"
                self.num -= 40
            elif self.num >= 10 :
                roman = roman + "X"
                self.num -= 10
            elif self.num >= 9 :
                roman = roman + "IX"
                self.num -= 9
            elif self.num >= 5 :
                roman = roman + "V"
                self.num -= 5
            elif self.num >= 4 :
                roman = roman + "IV"
                self.num -= 4
            elif self.num >= 1 :
                roman = roman + "I"
                self.num -= 1
        return roman

    def romanToDeci(self, s):
        self.s = s
        num = 0
        while len(self.s) > 0 :
            if self.s[0] == "M" :
                num += 1000
                self.s = self.s[1:]
            elif self.s[0] == "C" and self.s[1] == "M" :
                num += 900
                self.s = self.s[2:]
            elif self.s[0] == "D" :
                num += 500
                self.s = self.s[1:]
            elif self.s[0] == "C" and self.s[1] == "D" :
                num += 400
                self.s = self.s[2:]
            elif self.s[0] == "C" and self.s[1] != "M" and self.s[1] != "D" :
                num += 100
                self.s = self.s[1:]
            elif self.s[0] == "X" :
                if self.s[1] == "C" :
                    num += 90
                    self.s = self.s[2:]
                elif self.s[1] == "L" :
                    num += 40
                    self.s = self.s[2:]
                else :
                    num += 10
                    self.s = self.s[1:]
            elif self.s[0] == "L" :
                num += 50 
                self.s = self.s[1:]
            elif self.s[0] == "I" :
                if len(self.s) > 1 and self.s[1] == "x" :
                    num += 9
                    self.s = self.s[2:]
                elif len(self.s) > 1 and self.s[1] == "V" :
                    num += 4
                    self.s = self.s[2:]
                else :
                    num += 1
                    self.s = self.s[1:]
            elif self.s[0] == "V" :
                num += 5
                self.s = self.s[1:]
        return num

num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))

print(translator().romanToDeci(translator().deciToRoman(num)))