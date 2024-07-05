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

class Solution(ListNode):
    def deleteNode(self, node):
        head=self
        remeber=self
        if self==None:
            pass
        elif self.next==None:
            if self.val==node.val:
                self=None
            else:
                pass
        else:
            while(remeber.next!=None):
                if self.val!=node.val:
                    remeber=self
                    self=self.next
                else:
                    if self==head:
                        self=self.next
                    else:
                        remeber.next=self.next
                        self.next=None
                        self=remeber.next




        pass

if __name__=="__main__":
    head = [4, 5, 1, 9]
    node = ListNode(4)


    A=Solution()
    A.create_a_linked_list_from_list(head)
    A.deleteNode(node)
    A.show()

    # B=A.deleteNode(ls_num,node)
    # B.show()

    'chua giai quyet duoc'