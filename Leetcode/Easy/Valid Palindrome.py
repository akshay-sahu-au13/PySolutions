## https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:

        S = ""
        for i in s:
            if i.isalnum():
                S += i
        return S.lower() == S[::-1].lower()