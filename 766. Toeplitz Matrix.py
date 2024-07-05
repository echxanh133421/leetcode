class Solution:
    def isToeplitzMatrix(self, matrix) -> bool:
        row=len(matrix)
        col=len(matrix[0])
        for i in range(col):
            #xac dinh sub_matrix
            ls1=[]
            len_sq_matrix_sub=min(col-i,row)
            #print(len_sq_matrix_sub)
            sub_matrix=[]
            for j in range(0,len_sq_matrix_sub):
                ls=[]
                for k in range(i,i+len_sq_matrix_sub):
                    ls.append(matrix[j][k])
                sub_matrix.append(ls)
            print(sub_matrix)
            for j in range(len(sub_matrix)):
                ls1.append(sub_matrix[j][j])
            a=list(set(ls1))
            if len(a)>1:
                return False
        return True
if __name__=="__main__":
    matrix=[[36,59,71,15,26,82,87],
            [56,36,59,71,15,26,82],
            [15,0,36,59,71,15,26]]
    a=Solution()
    b=a.isToeplitzMatrix(matrix)
    print(b)
    '''chua dung'''
