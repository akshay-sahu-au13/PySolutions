def longestValidParentheses(A):

    l = r = maxL = 0

    for i in range(len(A)):

        if A[i] == "(":
            l += 1
        else:
            r += 1

        if l == r:
            maxL = max(maxL, r*2)
        elif r > l:
            l = r = 0

    l = r = 0

    for i in range(len(A) - 1, -1, -1):

        if A[i] == '(':
            l += 1
        else:
            r += 1

        if l == r:
            maxL = max(maxL, 2 * l)

        elif l > r:
            l = r = 0

    return maxL


if __name__ == "__main__":
    A = input("Enter the parentheses: ")
    print(longestValidParentheses(A))
