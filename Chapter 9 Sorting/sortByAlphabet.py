inp = input("Enter Input : ").split()
alphabetInput = []

for data in inp:
    for char in data:
        if char.isalpha():
            alphabetInput.append([char,data])
            break

for i in range(len(alphabetInput)-1):
    for j in range(len(alphabetInput)-i-1):
        if ord(alphabetInput[j][0]) > ord(alphabetInput[j+1][0]):
            temp = alphabetInput[j]
            alphabetInput[j] = alphabetInput[j+1]
            alphabetInput[j+1] = temp

for data in alphabetInput:
    print(data[1],end=' ')
print()