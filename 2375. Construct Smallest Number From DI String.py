class Solution:
    def smallestNumber(self, pattern: str) :
        ls_num=[]
        for i in range(len(pattern)+1):
            ls_num.append(i+1)

        number_i=pattern.count('I')
        number_d=pattern.count('D')

        ls_num_i=ls_num[0:number_i]
        ls_num_d=ls_num[number_i:]


        ls_final=''
        start_i=1
        for i in range(len(pattern)):
            if pattern[i]=='I':
                ls_final+=str(start_i)
                start_i+=1
                i+=1
            else:
                count=0
                while True:
                    if pattern[i]=='D':
                        count+=1
                        i+=1
                    else:
                        break
                    if i>=len(pattern):
                        break
                if i==len(pattern):
                    while count!=0:
                        ls_final += str(ls_num_d[count])
                        count-=1
                    break
                else:
                    for j in range(count-1,-1,-1):
                        ls_final+=str(ls_num_d[j])
                    ls_num_d=ls_num_d[count:]
        for i in ls_num_d:
            if str(i) not in ls_final:
                ls_final+=str(i)
                break
        return ls_final




if __name__=="__main__":
    a=Solution()
    pattern = "IIIDIDDD"
    b=a.smallestNumber(pattern)
    print(b)

    '''chua gia quyet duoc'''