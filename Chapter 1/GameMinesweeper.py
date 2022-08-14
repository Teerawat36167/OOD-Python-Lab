def num_grid(lst):
    for y in range(5) :
        for x in range(5) :
            if lst[y][x] == "#" :
                continue
            count = 0
            def check(xpos,ypos) :
                return ypos in range(5) and xpos in range(5) and (lst[ypos][xpos] == "#")
            if check(x-1,y-1):
                count += 1
            if check(x,y-1) :
                count += 1
            if check(x+1,y-1) :
                count += 1
            if check(x-1,y):
                count += 1
            if check(x+1,y):
                count += 1
            if check(x-1,y+1):
                count += 1
            if check(x,y+1):
                count += 1
            if check(x+1,y+1):
                count += 1
            lst[y][x] = str(count)
    return lst

lst_input = []

print("*** Minesweeper ***")
input_list = input("Enter input(5x5) : ").split(",")

for e in input_list:

    lst_input.append([i for i in e.split()])

print("\n",*lst_input,sep = "\n")

print("\n",*num_grid(lst_input),sep = "\n")