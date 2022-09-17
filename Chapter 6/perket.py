def perket(inp) :
    combiList = combi(inp)
    minPerket = 1000000000
    
    for i in combiList :
        if len(i) == 0 :
            continue
        else :
            s = 1
            b = 0
            for j in i :
                sAndb = j.split(" ")
                s *= int(sAndb[0])
                b += int(sAndb[1])
            sumPerket = abs(s-b)
            if sumPerket < minPerket :
                minPerket = sumPerket

    return minPerket

def combi(ls) :
    if len(ls) == 0 :
        return [[]]

    comb = []
    for i in combi(ls[1:]) :
        comb += [i, i + [ls[0]]]

    return comb

inp = input("Enter Input : ").split(",")

print(perket(inp))