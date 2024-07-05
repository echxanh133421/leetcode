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
    def len(self,head):
        if head==None:
            return 0
        elif head.next==None:
            return 1
        else:
            l=1
            while head.next!=None:
                l+=1
                head=head.next
            return l
    def swapNodes(self, head, k):
        '''....'''
        head1=head
        head2=head
        l=k
        head3=head
        if head.next==None:
            return head
        else:
            while k!=1:
                head1=head1.next
                k-=1
            f=self.len(head)-l
            while f:
                head2=head2.next
                f-=1
            swap=head1.val
            head1.val=head2.val
            head2.val=swap
            return head3



            pass

if __name__=="__main__":
    head = [1, 2, 3, 4, 5]
    k = 2
    ls_num=ListNode()
    ls_num.create_a_linked_list_from_list(head)


    a=Solution()
    b=a.swapNodes(ls_num,k)
    b.show()
    # b=a.len(ls_num)
    # print(b)