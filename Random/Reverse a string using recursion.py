## Q1. Reverse a string using recurssion

def Reverse(S):
    if len(S) == 0:
        return ""
    R = Reverse(S[1:]) + S[0] 
    return   R

S = "AkshaySahu"
print(Reverse(S))