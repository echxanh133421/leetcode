

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
        len=1
        if head==None:
            return 0
        elif head.next==None:
            return 1
        else:
            while head.next!=None:
                head=head.next
                len+=1
            return len
    def rotateRight(self, head, k: int):
        node=head
        #remeber=head
        if head==None:
            return None
        elif head.next==None:
            return head
        else:
            k=k%self.len(head)
            while(k!=0):
                while head.next!=None:
                    remeber=head
                    head=head.next
                head.next=node
                remeber.next=None
                k-=1
                node=head
            return head








if __name__=="__main__":

    head = [1,2,3,4,5]
    k = 2
    ls_num=ListNode()
    ls_num.create_a_linked_list_from_list(head)
    #ls_num.show()

    A=Solution()
    B=A.rotateRight(ls_num,k)
    B.show()

    pass