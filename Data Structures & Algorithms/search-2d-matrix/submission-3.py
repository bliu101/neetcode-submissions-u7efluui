class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # treat matrix like a big array to bst
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS * COLS - 1
        while l <= r:
            m = l + ((r - l)//2)
            # find the matrix coords of m
            row, col = m // COLS, m % COLS
            if target < matrix[row][col]:
                r = m - 1
            elif target > matrix[row][col]:
                l = m + 1
            else:
                return True
        return False
            