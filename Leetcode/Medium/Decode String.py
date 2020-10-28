## https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str: 
        res = []
        for i in s:
            decode = ""
            if i == "]":
                while res and res[-1] != "[":
                    decode += res.pop()
                res.pop()

                k = 0
                base = 1
                while res and res[-1].isdigit():
                    k += int(res.pop())*base
                    base *= 10

                decode *= k
                for j in decode[::-1]:
                    res.append(j)
                
            else:
                res.append(i)

        return "".join(res)

# Driver function to check the program:
if __name__ == "__main__":
    S = Solution()
    Str = ["2[abc]3[cd]ef","3[a2[c]]","3[a]2[bc]","abc3[cd]xyz"]
    for i in Str:
        print(f"For code {i}, the decoded string is: ", end = " ")
        print(S.decodeString(i))
        print()
                