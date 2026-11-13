from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        # 1. Pre-populate sets with existing numbers and record empty cells
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    empty_cells.append((r, c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)

        # 2. Backtracking helper function
        def backtrack(idx: int) -> bool:
            # Base case: all empty cells have been filled
            if idx == len(empty_cells):
                return True

            r, c = empty_cells[idx]
            box_id = (r // 3) * 3 + (c // 3)

            for num in "123456789":
                if num not in rows[r] and num not in cols[c] and num not in boxes[box_id]:
                    # Place the number
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_id].add(num)

                    # Move to the next empty cell
                    if backtrack(idx + 1):
                        return True

                    # Undo placement (backtrack) if it didn't lead to a solution
                    board[r][c] = '.'
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box_id].remove(num)

            return False

        backtrack(0)
