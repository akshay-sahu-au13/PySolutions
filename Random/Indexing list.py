items = ["pens", "pencils", "books", "Rubbers"]

qty = [10, 5, 6, 3]

print("I have ", end = "")

for i in range(0,4):

    if i == 2:
        print(qty[i], items[i], end =" and "  )
    elif i == 3:
        print(qty[i], items[i], end ="."  )
    else:
        print(qty[i], items[i], end =", "  )