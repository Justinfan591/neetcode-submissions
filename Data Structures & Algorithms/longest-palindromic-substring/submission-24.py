class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        lenres = 1
        res = s[0]
        for i in range(len(s)):
            for offset in (0, 1):
                j = 0
                while (i - j >= 0) and (i + j + offset < len(s)) and s[i-j] == s[i+j+offset]:
                    j += 1
                if 2*j - 1 + offset > lenres:
                    lenres = 2*j - 1 + offset
                    res = s[i-j+1 : i+j+offset]
        return res