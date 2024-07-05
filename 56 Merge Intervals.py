class Solution:
    def merge(self, intervals) :
        # ls=[]
        # for i in intervals:
        #     for j in range(i[0],i[1]+1):
        #         ls.append(j)
        # ls2=list(set(ls))
        # ls_final=[]
        # ls2.sort()
        # ls_sub = []
        # for i in range(min(ls2),max(ls2)+1):
        #     if i in ls2:
        #         ls_sub.append(i)
        #     else:
        #         if len(ls_sub)!=0:
        #             ls_final.append(ls_sub)
        #         ls_sub=[]
        #     if i==max(ls2):
        #         ls_final.append(ls_sub)
        # ls_3=[]
        # for i in ls_final:
        #     ls_sub=[i[0],i[-1]]
        #     ls_3.append(ls_sub)
        # return ls_3
        for i in range(len(intervals)-1):
            for j in range(i+1,len(intervals)):
                if intervals[i][0]>intervals[j][0]:
                    swap=intervals[i]
                    intervals[i]=intervals[j]
                    intervals[j]=swap
        i=0
        while i<len(intervals)-1:
            if intervals[i+1][0]>=intervals[i][0] and intervals[i+1][0]<=intervals[i][1]:
                if intervals[i+1][1]>=intervals[i][0] and intervals[i+1][1]<=intervals[i][1]:
                    intervals[i:i + 2] = [[intervals[i][0], intervals[i][1]]]
                else:
                    intervals[i:i+2]=[[intervals[i][0],intervals[i+1][1]]]
                i-=1
            i+=1

        return intervals



if __name__=="__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    a=Solution()
    print(a.merge(intervals))