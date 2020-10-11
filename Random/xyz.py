for i in range(0,4):
    for j in range(0,4):
        print(i, end=" ")
        if j >= 2:
            print("")
            break
        print(j)
    print("")