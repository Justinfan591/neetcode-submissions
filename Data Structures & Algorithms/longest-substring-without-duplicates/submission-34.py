class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        found = {}
        l = 0
        r = 0
        best = 1
        charend = 'o'
        endr = 0
        endl = 0

        while r < len(s): 
            char = s[r]
            if char in found and found[char] >=l: 
                if best < r - l: 
                    best = r- l
                    charend = char
                    endr = r
                    endl = l

                l = found[char] + 1
                found[char] = r
            else: found[char] = r
            r += 1
        best = max(best, r-l)
        print(charend, endr,endl,l,r)
        return best
