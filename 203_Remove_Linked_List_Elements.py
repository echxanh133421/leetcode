

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
    def removeElements(self, head, val: int):
        node=head
        remeber=head
        if head==None:
            return None
        elif head.next==None:
            if head.val==val:
                return None
            else:
                return head
        else:
            while remeber.next!=None:
                if head==None:
                    return None
                if head.val==val :
                    if head==node:
                        head=head.next
                        node=head
                    else:
                        remeber.next=head.next
                        head.next=None
                        head=remeber.next
                else:
                    remeber=head
                    head=head.next

            return node




        pass

if __name__=="__main__":
    head = [1,2,3,6,4,5,6]
    val= 6
    ls_num = ListNode()
    ls_num.create_a_linked_list_from_list(head)

    A=Solution()
    B=A.removeElements(ls_num,val)
    B.show()
    pass