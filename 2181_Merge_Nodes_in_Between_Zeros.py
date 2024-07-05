

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
    def mergeNodes(self, head):
        list_final=[]
        node=head
        a=node
        if head==None:
            return None
        elif head.next==None:
            return None
        else:
            while head.next!=None:
                if head.val==0:
                    sum=0
                    head=head.next
                    while(head.val!=0):
                        sum+=head.val
                        head=head.next
                    # list_final.append(sum)
                    node.val=sum
                    nho=node
                    node=node.next
            nho.next=None
            return a
            # return list_final
        pass


if __name__=="__main__":

    ls_num=[0,3,1,0,4,5,2,0]
    list_number=ListNode()
    list_number.create_a_linked_list_from_list(ls_num)

    # list_number.show()

    A=Solution()
    b=A.mergeNodes(list_number)
    b.show()

    pass