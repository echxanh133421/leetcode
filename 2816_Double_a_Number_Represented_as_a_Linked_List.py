
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
    def doubleIt(self, head):
        ls_num=[]
        while head!=None:
            ls_num.append(head.val)
            head=head.next

        ls_num_double=[]
        remember=0

        for i in range(len(ls_num)-1,-1,-1):
            num=ls_num[i]*2+remember
            if num>10:
                ls_num_double.append(int(num%10))
                remember=1
            else:
                ls_num_double.append(int(num))
                remember=0
        if remember==1:
            ls_num_double.append(remember)
        ls_num_double.reverse()

        node=ListNode(ls_num_double[0])
        head1=node
        for i in range(1,len(ls_num_double)):
            node2=ListNode(int(ls_num_double[i]))
            node.next=node2
            node=node.next
        return head1

if __name__=="__main__":
    num=[1, 8, 9]
    a=ListNode()
    a.create_a_linked_list_from_list(num)
    A=Solution()
    b=A.doubleIt(a)
    b.show()