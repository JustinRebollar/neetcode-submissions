class NumMatrix:
    numMatrix = [0][0]

    def __init__(self, matrix: List[List[int]]):
        self.numMatrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0

        for i in range(len(self.numMatrix)):
            for j in range(len(self.numMatrix[i])):
                if (i >= row1 and i <= row2):
                    if (j >= col1 and j <= col2):
                        sum += self.numMatrix[i][j]

        return sum
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)