def checkvalidity(Str):
    op = 0
    cp = 0
    for i in Str:
        if i == "(":
            op+=1
        else:
            cp +=1
        if cp>op:
            return False
        
    return cp==op

def parentheses(n, Str):
    if len(Str) == 2*n:
        if checkvalidity(Str):
            print(Str)
        return 1

    parentheses(n, Str+"(")
    parentheses(n, Str+")")

parentheses(7,"")
