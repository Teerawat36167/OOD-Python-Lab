def gcd(a, b) :
     if b == 0 :
          return a
     else :
          return gcd(b, a % b)

a, b = input("Enter Input : ").split(" ")

if abs(int(a)) < abs(int(b)) :
     a, b = b, a

if int(a) == 0 and int(b) == 0 :
     print("Error! must be not all zero.")
else :
     ans = abs(gcd(int(a),int(b)))
     if int(b) == 0 and int(a) < 0 :
          a, b = b, a
     print(f'The gcd of {a} and {b} is : {ans}')