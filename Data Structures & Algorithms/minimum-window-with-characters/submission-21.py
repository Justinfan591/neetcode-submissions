class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #l,r move right until t is included in s, then move l and move r when not included again. Find best/shortest
        best = ""
        l = 0
        t_dic = {}
        s_dic = {}
        check = True
        for char in t: 
            t_dic[char] = 1 + t_dic.get(char, 0)
        def included(dicS, dicT):
            for c,n in dicT.items(): 
                if n > dicS.get(c,0):
                    return False
            return True
        best_l, best_r = 0, len(s)
        for r in range(len(s)): 
            s_dic[s[r]] = 1 + s_dic.get(s[r], 0)

            while included(s_dic,t_dic):
                if best == "" and check:
                    best_l = l
                    best_r = r
                    check = False
                if r-l+1 < best_r-best_l+1: 
                    best_l = l
                    best_r = r
                s_dic[s[l]] -= 1
                l += 1
        if check: 
            return ""
         
        return s[best_l:best_r+1]
