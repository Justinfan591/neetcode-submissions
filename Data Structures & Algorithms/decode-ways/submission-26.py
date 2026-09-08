from functools import cache

class Solution:
    def numDecodings(self, s: str) -> int:
        #if there is a 0 there must be a number in the front
        #wait but; break it by one digit or 2 digits; assume numDecodings work
        dic = {}
        def dp(s):
            #base case
            # means it is correct first 2 digits s=="""
            if s in dic: 
                return dic[s]
            if (len(s) == 1 and s!='0') or s == "":
                return 1
            if s[0] == '0': 
                return 0
            if len(s)>=2 and int(s[:2]) <= 26: 
                result = dp(s[1:]) + dp(s[2:])
                dic[s] = result
                return result
            else: 
                result = dp(s[1:]) 
                dic[s] = result
                return result
            
        return dp(s)

    