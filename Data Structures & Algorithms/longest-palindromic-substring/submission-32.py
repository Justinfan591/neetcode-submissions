class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        lenres = 0 

        for i in range(len(s)): 
            #odd cases
            l, r = i,i
            while l >= 0 and r < len(s) and s[l] == s[r]: 
                if (r-l+1) > lenres: 
                    lenres = r-l+1 
                    res = s[l:r+1]
                l-=1
                r+=1
            #even cases
            l, r = i,i+1
            while l >= 0 and r < len(s) and s[l] == s[r]: 
                if (r-l+1) > lenres: 
                    lenres = r-l+1 
                    res = s[l:r+1]
                l-=1
                r+=1
        return res