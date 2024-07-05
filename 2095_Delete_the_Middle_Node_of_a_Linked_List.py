
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
        a=head
        if head==None:
            return 0
        elif head.next==None:
            return 1
        else:
            l=1
            while head.next!=None:
                l+=1
                head=head.next
            head=a
            return l

    def deleteMiddle(self, head) :
        if head.next==None:
            return None
        else:
            mid=int(self.len(head)/2)
            a=head
            while mid!=1:
                mid-=1
                head=head.next
            head.next=head.next.next
            return a

if __name__=="__main__":
    nums=[1,2,3,4]
    a=ListNode()
    a.create_a_linked_list_from_list(nums)
    A=Solution()
    b=A.deleteMiddle(a)
    b.show()