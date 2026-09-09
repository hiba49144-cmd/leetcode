class Solution(object):
    def solveSudoku(self, board):

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    num = board[r][c]
                    b = (r // 3) * 3 + (c // 3)

                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[b].add(num)

        def backtrack():

            best_cell = None
            best_candidates = None

           
            for r in range(9):
                for c in range(9):

                    if board[r][c] == '.':
                        b = (r // 3) * 3 + (c // 3)

                        candidates = set("123456789") \
                            - rows[r] \
                            - cols[c] \
                            - boxes[b]

                        if not candidates:
                            return False

                        if (best_candidates is None or
                                len(candidates) < len(best_candidates)):

                            best_candidates = candidates
                            best_cell = (r, c)

                            
                            if len(candidates) == 1:
                                break

                if best_candidates is not None and len(best_candidates) == 1:
                    break

            
            if best_cell is None:
                return True

            r, c = best_cell
            b = (r // 3) * 3 + (c // 3)

            for num in best_candidates:

                board[r][c] = num
                rows[r].add(num)
                cols[c].add(num)
                boxes[b].add(num)

                if backtrack():
                    return True

            
                board[r][c] = '.'
                rows[r].remove(num)
                cols[c].remove(num)
                boxes[b].remove(num)

            return False

        backtrack()
        