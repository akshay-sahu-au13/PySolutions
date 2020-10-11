
def rev_str():

    X = input("Enter a string:")
    L = len(X)-1
    S = ""

    for i in range(L, -1,-1):

        print(X[i]+S, end = "")

rev_str()

     