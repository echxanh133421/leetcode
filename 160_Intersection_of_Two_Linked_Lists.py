
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def show(self):
        print(self.val)
        while(self.next!=None):
            self=self.next
            print(self.val)

    def insert_a_node(self,data):
        node=ListNode(data)
        while(self.next!=None):
            self=self.next
        self.next=node

    def create_a_linked_list_from_list(self,arr):
        self.val=arr[0]
        for i in range(1,len(arr)):
            node=ListNode(arr[i])
            self.next=node
            self=self.next
    def remove_same_element(self):
        while(self.next!=None):
            while (self.val==self.next.val):
                self.next=self.next.next
                if self.next==None:
                    break
            self=self.next
            if self==None:
                break

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        a=headA
        b=headB
        ls_idA=[]
        ls_idB=[]
        while a!=None:
            ls_idA.append(id(a))
            a=a.next
        while b!=None:
            ls_idB.append(id(b))
            b=b.next
        check=0
        for i in range(len(ls_idA)):
            if ls_idA[i] in ls_idB:
                check=1
                id_check=i
                break
        if check==0:
            return None
        else:
            while id_check:
                headA=headA.next
                id_check-=1
            return headA

if __name__=="__main__":
    head1=ListNode(4)
    head1.next=ListNode(1)
    node_giao=ListNode(8)
    head1.next.next=node_giao
    head1.next.next.next=ListNode(4)
    head1.next.next.next.next=ListNode(5)

    head2=ListNode(5)
    head2.next=ListNode(6)
    head2.next.next=ListNode(1)
    head2.next.next.next=node_giao

    a=Solution()
    b=a.getIntersectionNode(head1,head2)
    print(b)

    '''giải quyết đưuọc'''