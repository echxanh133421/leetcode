class Solution:
    def hasGroupsSizeX(self, deck) -> bool:
        ls_set=list(set(deck))
        if len(ls_set)==1:
            return True
        number_check=deck.count(ls_set[0])
        for i in range(1,len(ls_set)):
            if deck.count(ls_set[i])!=number_check:
                return False
        return True

if __name__=="__main__":
    ls=[1]
    a=Solution()
    print(a.hasGroupsSizeX(ls))
    'chua giai quyet duoc'