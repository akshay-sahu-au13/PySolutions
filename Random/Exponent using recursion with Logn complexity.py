def power(x,n):
    if n ==0:
        return 1
    p = power(x,n//2)
    if n%2 ==0:
        return p*p
    else:
        return x*p*p

print(power(3,5))
