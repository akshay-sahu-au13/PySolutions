def round_off(n):

    n1 = int(n)
    n2 = n - n1

    if n2 >= 0.5:
        n = n1+1

    else:
        n = n1

    return n

print(round_off(12.6))
