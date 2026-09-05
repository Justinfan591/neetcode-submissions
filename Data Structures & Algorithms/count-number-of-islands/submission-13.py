class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid ==[]: 
            return
        island = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])
        
        def bfs(r, c):
            q = deque()
            directions = [[-1,0],[0,-1],[1,0],[0,1]]
            q.append([r,c])
            while q: 
                pos = q.popleft()
                r = pos[0]
                c = pos[1]
                for d in directions: 
                    dr = r + d[0]
                    dc = c + d[1]
                    if dr in range(0,rows) and dc in range(0,cols) and grid[dr][dc] == "1" and (dr,dc) not in visit:
                        visit.add((dr,dc))
                        q.append([dr,dc])
            return
        
        for r in range(rows):
            for c in range(cols): 
                if grid[r][c] == "1" and (r,c) not in visit: 
                    bfs(r,c)
                    island += 1
        return island

