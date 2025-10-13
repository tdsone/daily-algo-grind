# https://neetcode.io/problems/valid-sudoku?list=neetcode150


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def coord2box(i, j):
            candidates = None

            candidates = [k * 3 + j // 3 for k in range(3)]
            print(candidates)

            return candidates[i // 3]

        rows = []
        cols = []
        boxes = []
        for i in range(9):
            rows.append(set([i in range(9)]))
            cols.append(set([i in range(9)]))
            boxes.append(set([i in range(9)]))

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                try:
                    rows[i].remove(board[i][j])
                    cols[j].remove(board[i][j])
                    boxes[coord2box(i, j)].remove(board[i][j])
                except KeyError:
                    return False

        return True


"""
Approach 1: naive
- Go through each row and check if it's correct
- Go through each col ..
- Check each box

-> Visits each cell 3 times -> O(3n^2)

Approach 2:
- Assume we have one set of numbers (1 to 9) for each row, col and box
- We can just visit each cell once and remove number from respective sets
- each number occurs in three sets

-> runtime: O(n^2), space: O(3n^2) 

Observations: 
- there will be or no number to violate a constraint. constraint might be any of row, col or box
    - the violation will be to have the same number twice in a given row/col/box
    - we still have to check each number once

- Is there a subproblem that we solve repeatedly? 
"""
