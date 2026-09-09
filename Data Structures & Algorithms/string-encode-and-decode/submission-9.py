class Solution:

    def encode(self, strs: List[str]) -> str:
        # add the length of of the string and use # and number for length if string includes #
        res = ""
        for string in strs: 
            res = res + str(len(string)) + "#" + string
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 #start at 0
        l = 0
        r = 0
        
        while i in range(len(s)): 
            length = 0
            if s[i] == "#": 
                length = int(s[l:i])
                r = i + 1 + length
                res.append(s[i+1:r])
                i = i + length + 1
                l = i 
            i += 1
        return res
