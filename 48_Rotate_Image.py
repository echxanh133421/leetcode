class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix2=[]
        for i in range(len(matrix)-1,-1,-1):
            a=matrix[i]
            matrix2.append(a)
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j]=matrix2[j][i]
        return matrix

if __name__=="__main__":
    A=Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(A.rotate(matrix))

    """chua giai quyet duoc"""

