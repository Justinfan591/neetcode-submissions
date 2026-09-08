from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        #if there is a 0 there must be a number in the front
        #wait but; break it by one digit or 2 digits; assume numDecodings work
        @cache
        def dp(s):
            #base case
            # means it is correct first 2 digits s=="""
            if (len(s) == 1 and s!='0') or s == "":
                return 1
            if s[0] == '0': 
                return 0
            if len(s)>=2 and int(s[:2]) <= 26: 
                return dp(s[1:]) + dp(s[2:])
            else: return dp(s[1:])
            
        return dp(s)

    