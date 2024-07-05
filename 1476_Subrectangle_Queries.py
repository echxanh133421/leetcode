class SubrectangleQueries:

    def __init__(self, rectangle):
        self.maxtrix = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1,row2+1):
            for j in range(col1,col2+1):
                self.maxtrix[i][j]=newValue

    def getValue(self, row: int, col: int) -> int:
        return self.maxtrix[row][col]

if __name__=="__main__":
    matrix=[[1,2,3],[1,4,5],[4,5,6]]
    A=SubrectangleQueries(matrix)
    print(A.getValue(2,2))