

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
    def getDecimalValue(self, head):
        len=1
        number=0
        node=head
        if head==None:
            return None
        elif head.next==None:
            return head.val
        else:
            while(head.next!=None):
                len+=1
                head=head.next
            while(node.next!=0):
                number+=node.val*(2**(len-1))
                len-=1
                node=node.next
                if node==None:
                    break
            return number




if __name__=="__main__":
    list_binary_number=[1, 0, 1]
    linked_list=ListNode()
    linked_list.create_a_linked_list_from_list(list_binary_number)


    linked_list.show()

    A=Solution()
    number=A.getDecimalValue(linked_list)
    print(number)

    pass