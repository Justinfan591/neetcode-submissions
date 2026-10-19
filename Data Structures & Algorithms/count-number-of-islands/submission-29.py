class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == []: 
            return 0 
        num_island = 0
        #set that are visited
        visited = set()

        for row in range(len(grid)): 
            for col in range(len(grid[row])): 

                if (row,col) not in visited and grid[row][col] == "1": 
                    current = []
                    #stack
                    current.append((row,col))
                    num_island += 1
                    visited.add((row,col))
                    directions = [(-1,0),(0,-1),(1,0),(0,1)]
                    while current: 
                        curr = current.pop()
                        for direct in directions:
                            cur_row = curr[0]+direct[0]
                            cur_col = curr[1]+direct[1]
                            if cur_row in range(0,len(grid)) and cur_col in range(len(grid[0])) and grid[cur_row][cur_col] == "1" and (cur_row,cur_col) not in visited: 
                                visited.add((cur_row,cur_col))
                                current.append((cur_row,cur_col))
        return num_island



