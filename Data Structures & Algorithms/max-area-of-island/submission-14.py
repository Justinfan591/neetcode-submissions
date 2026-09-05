class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if grid ==[]: 
            return
        maxi = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])
        
        def bfs(r, c, maxi):
            q = deque()
            directions = [[-1,0],[0,-1],[1,0],[0,1]]
            q.append([r,c])
            temp = 1
            visit.add((r,c))
            while q: 
                pos = q.popleft()
                r = pos[0]
                c = pos[1]
                for d in directions: 
                    dr = r + d[0]
                    dc = c + d[1]
                    if dr in range(0,rows) and dc in range(0,cols) and grid[dr][dc] == 1 and (dr,dc) not in visit:
                        visit.add((dr,dc))
                        q.append([dr,dc])
                        temp += 1
            return temp
        
        for r in range(rows):
            for c in range(cols): 
                if grid[r][c] == 1 and (r,c) not in visit: 
                    temp = bfs(r,c,maxi)
                    if temp> maxi: 
                        maxi = temp
                    
        return maxi