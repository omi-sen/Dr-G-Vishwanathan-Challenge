class Solution:
    def findPeakGrid(self, mat: list[list[int]]) -> list[int]:
        low_col = 0
        high_col = len(mat[0]) - 1
        
        while low_col <= high_col:
            mid_col = (low_col + high_col) // 2
            
            # Find the row with the maximum element in the current mid_col
            max_row = 0
            for r in range(len(mat)):
                if mat[r][mid_col] > mat[max_row][mid_col]:
                    max_row = r
            
            # Determine values of the left and right neighbors
            left_val = mat[max_row][mid_col - 1] if mid_col - 1 >= 0 else -1
            right_val = mat[max_row][mid_col + 1] if mid_col + 1 < len(mat[0]) else -1
            
            # Check if the maximum element is a global 2D peak
            if mat[max_row][mid_col] > left_val and mat[max_row][mid_col] > right_val:
                return [max_row, mid_col]
            
            # If the left neighbor is greater, a peak must exist in the left half
            elif left_val > mat[max_row][mid_col]:
                high_col = mid_col - 1
                
            # Otherwise, a peak must exist in the right half
            else:
                low_col = mid_col + 1
                
        return [-1, -1]