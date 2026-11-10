class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        
        # Optimization: Early exit if the word is longer than the total number of cells
        if len(word) > ROWS * COLS:
            return False
            
        def dfs(r, c, index):
            # Base Case: All characters in the word have been matched
            if index == len(word):
                return True
                
            # Boundary and mismatch checks
            if (r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or 
                board[r][c] != word[index]):
                return False
            
            # Action: Mark the current cell as visited to prevent reuse
            temp = board[r][c]
            board[r][c] = "#"
            
            # Explore all 4 cardinal directions (Up, Down, Left, Right)
            found = (dfs(r + 1, c, index + 1) or
                     dfs(r - 1, c, index + 1) or
                     dfs(r, c + 1, index + 1) or
                     dfs(r, c - 1, index + 1))
            
            # Backtrack: Restore the original character for other search paths
            board[r][c] = temp
            
            return found

        # Traverse the grid to find a starting cell matching the first letter
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
                    
        return False
