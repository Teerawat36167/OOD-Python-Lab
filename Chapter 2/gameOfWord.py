class TorKham:

    def __init__(self):
        self.words = []

    def restart(self):
        self.words = []
        return "game restarted"

    def play(self, word):
        self.words.append(word)
        if str(word[:2]).lower() == str(self.words[len(self.words)-2][-2:]).lower() and len(self.words) > 1 :
            return "'" + word + "'" + " -> " + str(self.words)
        elif len(self.words) == 1 :
            return "'" + word + "'" + " -> " + str(self.words)
        else :
            return "'" + word + "'" + " -> game over"

torkham = TorKham()

print("*** TorKham HanSaa ***")


S = input("Enter Input : ").split(',')

while len(S) > 0 :
    if S[0][0] == "P" and len(S[0]) > 2:
        print(torkham.play(S[0][2:]))
        S = S[1:]
    elif S[0][0] == "R" :
        print(torkham.restart())
        S = S[1:]
    elif S[0][0] == "X" :
        break
    else :
        print("'" + S[0] + "' is Invalid Input !!!")
        break
