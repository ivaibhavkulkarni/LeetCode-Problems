class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])
        
        # To store cells that can flow into the Pacific and Atlantic oceans
        pacific_reachable = [[False] * n for _ in range(m)]
        atlantic_reachable = [[False] * n for _ in range(m)]
        
        # DFS function to mark reachable cells
        def dfs(r, c, reachable):
            reachable[r][c] = True
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if (0 <= nr < m and 0 <= nc < n and 
                    not reachable[nr][nc] and heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, reachable)

        # Start DFS from Pacific (left and top edges)
        for i in range(m):
            dfs(i, 0, pacific_reachable)      # Left edge (Pacific)
            dfs(i, n - 1, atlantic_reachable) # Right edge (Atlantic)
        for j in range(n):
            dfs(0, j, pacific_reachable)      # Top edge (Pacific)
            dfs(m - 1, j, atlantic_reachable) # Bottom edge (Atlantic)

        # Collect cells that can reach both oceans
        result = []
        for i in range(m):
            for j in range(n):
                if pacific_reachable[i][j] and atlantic_reachable[i][j]:
                    result.append([i, j])
        
        return result
