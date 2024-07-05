class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str):
        if len(s1)==1:
            if s1<s2:
                return s1*len(baseStr)
        ls=[]
        for i in range(len(s1)):
            ls.append([s1[i],s2[i]])

        i=0
        while i<len(ls)-1:
            j=i+1
            while j<len(ls):
                for k in range(len(ls[j])):
                    if ls[j][k] in ls[i]:
                        ls[i]+=ls[j]
                        ls[j]=[]
                        break
                j+=1
            i+=1
        # i = 0
        # while i < len(ls) - 1:
        #     j = i + 1
        #     while j < len(ls):
        #         for k in range(len(ls[j])):
        #             if ls[j][k] in ls[i]:
        #                 ls[i] += ls[j]
        #                 ls[j] = []
        #                 break
        #         j += 1
        #     i += 1

        ls_final=[]
        for i in range(len(ls)):
            if len(ls[i])!=0:
                a=list(set(ls[i]))
                a.sort()
                ls_final.append(a)


        str_final=''
        for i in range(len(baseStr)):
            for j in range(len(ls_final)):
                if baseStr[i] in ls_final[j]:
                    str_final+=ls_final[j][0]
                    break
                else:
                    if j==len(ls_final)-1:
                        str_final+=baseStr[i]
        return str_final

if __name__=="__main__":
    s1 ="cgokcgerolkgksgbhgmaaealacnsshofjinidiigbjerdnkolc"
    s2 ="rjjlkbmnprkslilqmbnlasardrossiogrcboomrbcmgmglsrsj"
    baseStr ="bxbwjlbdazfejdsaacsjgrlxqhiddwaeguxhqoupicyzfeupcn"
    a=Solution()
    b=a.smallestEquivalentString(s1,s2,baseStr)
    print(b)