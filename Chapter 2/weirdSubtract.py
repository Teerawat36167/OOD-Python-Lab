def weirdSubtract(n,k):
    for i in range(k) :
        strN = str(n)
        if strN[-1] == '0' :
            n //= 10
        elif strN[-1] != '0' :
            n -= 1
    return n

n,s = input("Enter num and sub : ").split()

print(weirdSubtract(int(n),int(s)))