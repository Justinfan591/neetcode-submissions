class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        ans = []

        def bfs(curR, curC):
            q = deque()
            visit = set()
            q.append([curR,curC])
            directions = [[-1,0],[0,-1],[1,0],[0,1],[0,0]]
            pac = False
            Atlantic = False
            #base case

            while q:
                pos = q.popleft()
                height = heights[pos[0]][pos[1]]
                curR = pos[0]
                curC = pos[1]
                for move in directions: 
                    dr = curR + move[0]
                    dc = curC + move[1]
                    if dr in range(0,rows) and dc in range(0,cols) and height >= heights[dr][dc] and (dr,dc) not in visit: 
                        q.append([dr,dc])
                        visit.add((dr,dc))
                        if dr == 0 or dc == 0: 
                            pac = True
                        if dr == rows - 1 or dc == cols - 1: 
                            Atlantic = True
                    if pac and Atlantic: 
                        return True
            if pac and Atlantic: 
                return True
            return False
        for r in range(rows): 
            for c in range(cols): 
                if bfs(r,c): 
                    ans.append([r,c])
        
        return ans