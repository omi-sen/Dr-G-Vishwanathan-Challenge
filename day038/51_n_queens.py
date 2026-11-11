class Solution:
        def solveNQueens(self, n: int) -> list[list[str]]:
                res = []
                        board = [["."] * n for _ in range(n)]
                                cols = set()
                                        pos_diag = set()  # row + col
                                                neg_diag = set()  # row - col

                                                        def backtrack(r: int) -> None:
                                                                    if r == n:
                                                                                    res.append(["".join(row) for row in board])
                                                                                                    return

                                                                                                                for c in range(n):
                                                                                                                                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                                                                                                                                                    continue

                                                                                                                                                                    cols.add(c)
                                                                                                                                                                                    pos_diag.add(r + c)
                                                                                                                                                                                                    neg_diag.add(r - c)
                                                                                                                                                                                                                    board[r][c] = "Q"

                                                                                                                                                                                                                                    backtrack(r + 1)

                                                                                                                                                                                                                                                    # Backtrack
                                                                                                                                                                                                                                                                    cols.remove(c)
                                                                                                                                                                                                                                                                                    pos_diag.remove(r + c)
                                                                                                                                                                                                                                                                                                    neg_diag.remove(r - c)
                                                                                                                                                                                                                                                                                                                    board[r][c] = "."

                                                                                                                                                                                                                                                                                                                            backtrack(0)
                                                                                                                                                                                                                                                                                                                                    return res
                                                                                                                                                                                                                                                                                                                                    