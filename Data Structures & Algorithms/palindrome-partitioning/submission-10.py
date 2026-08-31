class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []
        
        def dfs(i): 
            #base case
            if i >= len(s):
                res.append(subset.copy())
                return 
            for j in range(i,len(s)): 
                if self.isPali(s[i:j+1]):
                    subset.append(s[i:j + 1])
                    dfs(j + 1)
                    subset.pop()
                    
        dfs(0)
        return res

    def isPali(self, s: str): 
        l = 0
        r = len(s)-1
        while l<r: 
            if s[l]!=s[r]:
                return False
            l = l+1
            r = r -1
        return True

                

