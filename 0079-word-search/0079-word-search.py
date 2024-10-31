class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c, index):
            # If we’ve matched the entire word, return True
            if index == len(word):
                return True
            # If out of bounds or the cell doesn't match the word character
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
                return False
            
            # Mark the cell as visited by temporarily changing its value
            temp = board[r][c]
            board[r][c] = '#'
            
            # Explore all four directions
            found = (dfs(r+1, c, index+1) or
                     dfs(r-1, c, index+1) or
                     dfs(r, c+1, index+1) or
                     dfs(r, c-1, index+1))
            
            # Restore the cell's original value (backtracking)
            board[r][c] = temp
            return found

        # Try to start DFS from every cell in the grid
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False