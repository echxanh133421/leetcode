class Solution:
    def subdomainVisits(self, cpdomains) :
        number=[]
        dmain=[]
        for i in cpdomains:
            for j in range(len(i)):
                if i[j]==' ':
                    number.append(int(i[:j]))
                    dmain.append(i[j+1:])
        ls_dmain=[]
        for i in range(len(dmain)):
            ls=[]
            a=dmain[i].split('.')
            for j in range(len(a)-1,-1,-1):
                if j==len(a)-1:
                    s=a[-1]
                    ls.append(s)
                else:
                    s=''
                    for k in range(j,len(a)):
                        if k==len(a)-1:
                            s+=a[-1]
                        else:
                            s+=a[k]+'.'
                    ls.append(s)
            ls_dmain.append(ls)

        ls_dmain1=[]

        for i in range(len(ls_dmain)):
            ls_dmain1+=ls_dmain[i]

        ls_dmain2=list(set(ls_dmain1))

        ls_final=[]
        for i in ls_dmain2:
            sum=0
            for j in range(len(cpdomains)):
                if i in cpdomains[j]:
                    sum+=number[j]
            ls_final.append(str(sum)+' '+i)

        return ls_final

if __name__=='__main__':
    a=Solution()
    cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    b=a.subdomainVisits(cpdomains)
    print(b)