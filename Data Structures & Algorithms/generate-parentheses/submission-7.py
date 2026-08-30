class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # () -> ()() or (()) add separate and outside
        res = []
        def dfs(cur, opened, closed):
            #base case
            if len(cur) == n*2:
                if opened == closed:
                    res.append(cur)
                return
            
            #recursive step
            if opened > closed: 
                dfs(cur+")",opened,closed + 1)
                dfs(cur+"(", opened + 1, closed)
            else: 
                dfs(cur+"(", opened + 1, closed)
        dfs("",0,0)

        return res