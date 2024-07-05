class Solution:
    def modifiedMatrix(self, matrix) :
        ls=[]
        for i in range(len(matrix[0])):
            ls_sub=[]
            for j in range(len(matrix)):
                ls_sub.append(matrix[j][i])
            ls.append(ls_sub)

        for i in range(len(ls)):
            for j in range(len(ls[0])):
                if ls[i][j]==-1:
                    a=max(ls[i])
                    ls[i][j]=a
        ls1=[]
        for i in range(len(ls[0])):
            ls1_sub=[]
            for j in range(len(ls)):
                ls1_sub.append(ls[j][i])
            ls1.append(ls1_sub)
        return ls1
