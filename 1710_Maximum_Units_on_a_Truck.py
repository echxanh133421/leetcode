class Solution:
    def maximumUnits(self, boxTypes, truckSize: int) -> int:
        #sort
        for i in range(0,len(boxTypes)-1):
            for j in range(i+1,len(boxTypes)):
                if boxTypes[i][1]<boxTypes[j][1]:
                    swap_ls=boxTypes[i]
                    boxTypes[i]=boxTypes[j]
                    boxTypes[j]=swap_ls
        total_unit=0
        i=0
        while truckSize!=0 and i<len(boxTypes):
            if truckSize>boxTypes[i][0]:
                total_unit+=boxTypes[i][0]*boxTypes[i][1]
                truckSize-=boxTypes[i][0]
            else:
                total_unit+=boxTypes[i][1]*truckSize
                truckSize=0
            i+=1
        return total_unit

if __name__=="__main__":
    boxTypes =[[1, 3], [5, 5], [2, 5], [4, 2], [4, 1], [3, 1], [2, 2], [1, 3], [2, 5], [3, 2]]
    truckSize=35
    A=Solution()
    print(A.maximumUnits(boxTypes,truckSize))