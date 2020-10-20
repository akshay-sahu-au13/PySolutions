##Q2. Calculate factorial using recursion

def Factorial(N):

    if N == 1:
        return 1


    Res = N * Factorial(N-1)
    return Res

print(Factorial(6))