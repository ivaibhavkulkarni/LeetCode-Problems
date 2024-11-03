class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        # Dimensions of the grid
        m, n = len(grid), len(grid[0])

        # Helper function to perform DFS
        def dfs(i, j):
            # Check if we are out of bounds or on water ('0')
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
                return
            # Mark the current cell as visited
            grid[i][j] = '0'
            # Visit all neighboring cells
            dfs(i + 1, j)  # Down
            dfs(i - 1, j)  # Up
            dfs(i, j + 1)  # Right
            dfs(i, j - 1)  # Left

        island_count = 0

        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':  
                    dfs(i, j)  
                    island_count += 1 

        return island_count