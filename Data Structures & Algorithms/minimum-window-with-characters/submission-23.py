class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for c in t:
            need[c] = 1 + need.get(c, 0)

        window = {}
        have, required = 0, len(need)   # distinct chars currently satisfied / needed
        best_l, best_r = 0, len(s)
        l = 0

        for r, c in enumerate(s):
            if c in need:
                window[c] = 1 + window.get(c, 0)
                if window[c] == need[c]:
                    have += 1           # c just became satisfied

            while have == required:
                if r - l < best_r - best_l:
                    best_l, best_r = l, r
                lc = s[l]
                if lc in need:
                    window[lc] -= 1
                    if window[lc] < need[lc]:
                        have -= 1       # lc just became unsatisfied
                l += 1

        return "" if best_r == len(s) else s[best_l:best_r + 1]