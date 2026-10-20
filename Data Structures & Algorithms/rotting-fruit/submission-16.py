class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #stack to store the current rotten ones and also the fresh ones
        #initalize the stacks
        rotten, count = [], -1

        for r in range(len(grid)): 
            for c in range(len(grid[0])): 
                value = grid[r][c]
                if value == 2: 
                    rotten.append((r,c))
        
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        temp = rotten # temp would let it in 
        while temp: 
            rotten = temp
            temp = []
            while rotten: 
                curr = rotten.pop()
                
                for direct in directions: 
                    row = direct[0] + curr[0]
                    col = direct[1] + curr[1]
                    if row in range(0,len(grid)) and col in range(0,len(grid[0])) and grid[row][col] == 1: 
                        temp.append((row,col))
                        grid[row][col] = 2
            count += 1
        
        for r in range(len(grid)): 
            for c in range(len(grid[0])): 
                value = grid[r][c]
                if value == 1: 
                    return -1
        if count == -1:
            return 0

        return count 