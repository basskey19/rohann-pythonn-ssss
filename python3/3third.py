for i in range (1,8):
    for j in range(1,8):
        print("$",end="")
    print()

for i in range(1,8):
    for j in range(1,i+7):
        print(j,end="")
    print()            