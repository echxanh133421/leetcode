class Solution:
    def deckRevealedIncreasing(self, deck ) :
        ls=[]
        i=len(deck)-1
        deck.sort()
        while i>=0:
            if ls==[]:
                ls.append(deck[i])
            else:
                a=ls[0:-1]
                b=[ls[-1]]
                ls=b+a
                ls.insert(0, deck[i])
            i-=1
        return ls

if __name__=="__main__":
    deck=[17,13,11,2,3,5,7]
    a=Solution()
    b=a.deckRevealedIncreasing(deck)
    print(b)