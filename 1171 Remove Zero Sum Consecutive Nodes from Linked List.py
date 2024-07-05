
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head):
        a=head
        ls=[]
        while a!=None:
            ls.append(a.val)
            a=a.next
        #return ls
        i=0
        while i<len(ls):
            if ls[i]==0:
                if i==0:
                    ls=ls[1:]
                elif i==len(ls)-1:
                    ls=ls[:-1]
                else:
                    ls=ls[:i]+ls[i+1:]
            else:
                i+=1
        i=0
        while i<len(ls):
            j=len(ls)-1
            while j>i:
                if sum(ls[i:j+1])==0:
                    a=ls[:i]
                    b=ls[j+1:]
                    ls=a+b
                    break
                else:
                    j-=1
            i+=1
        #return ls
        if len(ls)==0:
            return None
        else:
            a=ListNode()
            head=a
            i=0
            while i<len(ls):
                a.val=ls[i]
                if i==len(ls)-1:
                    break
                b=ListNode()
                a.next=b
                a=a.next
                i+=1
            return head


if __name__=="__main__":
    #head = [2,2,-2,1,-1,-1]
    a=ListNode(2)
    a.next=ListNode(2)
    a.next.next=ListNode(-2)
    a.next.next.next=ListNode(1)
    a.next.next.next.next=ListNode(-1)
    a.next.next.next.next.next=ListNode(-1)
    b=Solution()
    ls=b.removeZeroSumSublists(a)
    print(ls)
