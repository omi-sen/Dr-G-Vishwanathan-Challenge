class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        # Start at the top-right corner
        row = 0
        col = len(matrix[0]) - 1
        
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                # Target is smaller, move left to find smaller values
                col -= 1
            else:
                # Target is larger, move down to find larger values
                row += 1
                
        return False

        