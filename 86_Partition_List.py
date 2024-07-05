
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

    def partition(self, head, x: int) :
        head_a=None
        head_b=None
        A=None
        B=None
        if head==None:
            return None
        elif head.next==None:
            return head
        else:
            while head!=None:
                if head.val<x:
                    a=ListNode(head.val)
                    if head_a==None:
                        head_a=a
                        A=head_a
                    else:
                        head_a.next=a
                        head_a=head_a.next

                else:
                    b = ListNode(head.val)
                    if head_b == None:
                        head_b = b
                        B=head_b
                    else:
                        head_b.next = b
                        head_b = head_b.next
                head=head.next
            if A==None:
                return B
            if B==None:
                return A
            head_a.next=B
        return A

if __name__=="__main__":
    head=[1,1]
    x = 4

    ls=ListNode()
    ls.create_a_linked_list_from_list(head)

    #ls.show()
    A=Solution()
    B=A.partition(ls,x)
    B.show()