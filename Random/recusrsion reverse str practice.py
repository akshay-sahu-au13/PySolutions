# def rev(St):
#     if len(St)==0:
#         return ""
#     return rev (St[1:])+ St[0]
# print(rev("Akshay"))

## Sum of N natural numbers:

def Sum(N):
    if N == 1 :
        return 1
    return N + Sum(N-1)
print(Sum(10))

def power(n,ex):
    if ex == 0:
        return 1
    Exp = n*power(n,ex-1)

    return Exp
print(power(2,8))

def pow(x,exp):
    if exp == 0:
        return 1
    if exp%2 == 0:
        p = pow(x,exp//2)
    else:
        p = x*pow(x,exp//2)

    res = p*p

    return res
print(pow(3,30))
print(3**30)