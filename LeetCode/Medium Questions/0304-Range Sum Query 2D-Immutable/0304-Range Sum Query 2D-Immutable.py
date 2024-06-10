from typing import List

class NumMatrix:
    # This solution is not that optimal one
    # Calculates each row cumulative sum
    # Sums each row's range sum

    # Each call to sumRegion() is not O(1) but O(n)

    # There is a way to do this with a full cumulative sum matrix
    def __init__(self, matrix: List[List[int]]):
        self.cumSumMatrix = []
        for i in range(len(matrix)):
            cumSumRow = [matrix[i][0]]
            for j in range(1, len(matrix[i])):
                cumSumRow.append(matrix[i][j] + cumSumRow[j-1])
            self.cumSumMatrix.append(cumSumRow)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for i in range(row1, row2+1):
            if col1 == 0 or col2 == 0:
                print("Column 0")
                sum += self.cumSumMatrix[i][col2]
            else:
                sum += self.cumSumMatrix[i][col2] - self.cumSumMatrix[i][col1-1]
        return sum