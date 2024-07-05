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
    def reverseKGroup(self, head, k: int):
        if head.next==None:
            return head
        else:
            a=head
            ls_node=[]
            while head.next!=None:
                ls_node.append(head.val)
                head=head.next
            ls_node.append(head.val)


            ls_final=[]
            for i in range(0,len(ls_node),k):
                ls_in=ls_node[i:i+k]
                if len(ls_in)==k:
                    ls_in.reverse()
                ls_final+=ls_in

            head=a
            head1=head
            for i in range(len(ls_final)):
                head.val=ls_final[i]
                head=head.next
            return head1

if __name__=='__main__':
    head = [1, 2, 3, 4, 5]
    k = 3
    list_head=ListNode()
    list_head.create_a_linked_list_from_list(head)
    A=Solution()
    B=A.reverseKGroup(list_head,k)
    B.show()