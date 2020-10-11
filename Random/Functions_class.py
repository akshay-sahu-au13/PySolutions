def count_digit(Num):

    # Num = int(input("Enter a number: "))  # 1234

    Q = Num//10    # 123

    D = 1

    while Q != 0:

        Q = Q // 10
        D += 1

    print("Total digits in given number is: ", D)


count_digit(7645344)