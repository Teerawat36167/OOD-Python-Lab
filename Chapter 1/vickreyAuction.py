bid = input("Enter All Bid : ").split()

for i in range(0, len(bid)):
    bid[i] = int(bid[i])

bid.sort(reverse = True)

if len(bid) == 1 :
    print("not enough bidder")
elif len(bid) > 1 :
    if bid[0] > bid[1] :
        print("winner bid is "+str(bid[0])+ " need to pay "+str(bid[1]))
    elif bid[0] == bid[1] :
        print("error : have more than one highest bid")