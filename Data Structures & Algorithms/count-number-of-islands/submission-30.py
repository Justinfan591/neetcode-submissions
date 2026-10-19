class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            # Base case: Out of bounds or water -> stop exploring
            if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"  # Sink the land
            
            # Recursively explore all 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        num_islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    num_islands += 1
                    dfs(r, c)  # Completely sink the found island
                    
        return num_islands
