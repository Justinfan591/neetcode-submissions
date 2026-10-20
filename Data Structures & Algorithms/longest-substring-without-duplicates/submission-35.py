class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # two pointer problem 
        l, r = 0, 0
        dic = {}
        ans = 0

        while r < len(s): 
            if s[r] not in dic: 
                dic[s[r]] = 1
                r += 1
            else: # in dic
                length = r - l
                if length > ans: 
                    ans = length
                while s[l] != s[r]: 
                    del dic[s[l]]
                    l += 1
                #until we find in we increment another
                l += 1
                r += 1
        if len(s) - l > ans:
            ans = len(s) - l
        
        return ans
