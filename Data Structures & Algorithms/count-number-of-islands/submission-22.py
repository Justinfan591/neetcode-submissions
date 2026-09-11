class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == []: 
            return 0
        
        ans = 0
        visit = set()
        def dfs(r,c): 
            directions = [(-1,0),(1,0),(0,-1),(0,1)]

            for a,b in directions: 
                nr = r+a
                nc = c+b
                if nr in range(len(grid)) and nc in range(len(grid[0])) and grid[nr][nc] == "1" and (nr,nc) not in visit: 
                    visit.add((nr,nc))
                    dfs(nr,nc)
                
        
        for r in range(len(grid)):
            for c in range(len(grid[0])): 
                if grid[r][c] == "1" and (r,c) not in visit:
                    ans += 1
                    dfs(r,c)
        return ans

