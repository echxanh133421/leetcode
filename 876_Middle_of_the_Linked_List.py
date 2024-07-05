
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
    def middleNode(self, head):
        len=1
        key_id=0
        node=head
        if head==None:
            return None
        elif head.next==None:
            return head
        else:
            while(head.next!=None):
                len+=1
                head=head.next
            if len%2==0:
                key_id=int(len/2 + 1)
            else:
                key_id=int(len/2)+1
            # return key_id
            while(key_id-1):
                node=node.next
                key_id-=1
            return node

if __name__=="__main__":
    ls_nb=[1,2,3,4,5,6]
    list_number=ListNode()
    list_number.create_a_linked_list_from_list(ls_nb)

    # list_number.show()

    A=Solution()
    b=A.middleNode(list_number)
    b.show()