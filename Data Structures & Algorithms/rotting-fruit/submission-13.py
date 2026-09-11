class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshes = set()
        rots = deque() 

        #setting up the fresh and rot pos
        for r in range(len(grid)): 
            for c in range(len(grid[0])): 
                if grid[r][c] == 1: 
                    freshes.add((r,c))
                elif grid[r][c] == 2: 
                    rots.append((r,c))
        
        def infect(pos): 
            r = pos[0]
            c = pos[1]
            directs = [[-1,0],[0,-1],[1,0],[0,1]]

            for a,b in directs: 
                nr = r+a
                nc = c+b

                if nr in range(len(grid)) and nc in range(len(grid[0])) and (nr,nc) in freshes:
                    rots.append((nr,nc)) 
                    freshes.remove((nr,nc))

        #loop each rot 
        ans = 0
        
        while freshes and rots: 
            for i in range(len(rots)): 
                infect(rots.popleft())
            ans += 1
        
        if freshes: 
            return -1
        return ans