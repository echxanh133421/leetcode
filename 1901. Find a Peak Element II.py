class Solution:
    def check(self,mat,i,j):
        if mat[i][j]>mat[i][j-1] and mat[i][j]>mat[i][j+1] and mat[i][j]>mat[i+1][j] and mat[i][j]>mat[i-1][j]:
            return True
        return False
    def findPeakGrid(self, mat) :
        mat1=[]
        ls1=[-1]*(len(mat[0])+2)

        mat1.append(ls1)
        for i in range(len(mat)):
            mat1.append([-1]+mat[i]+[-1])
        mat1.append(ls1)

        for i in range(1,1+len(mat)):
            for j in range(1,len(mat[0])+1):
                if self.check(mat1,i,j):
                    return [i-1,j-1]


if __name__=='__main__':
    mat = [[1, 4], [3, 2]]
    a=Solution()
    b=a.findPeakGrid(mat)
    print(b)