def strrev(S):
    if len(S) == 1:
        return S

    return S[-1] + strrev(S[:len(S)-1])

print(strrev("Attainu"))
print(strrev("NamaN"))
print(strrev("Python Recurssion"))


      
