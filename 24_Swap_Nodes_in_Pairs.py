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
    def swapPairs(self, head) :
        if head == None:
            return None
        elif head.next == None:
            return head
        else:
            a = head
            b = head.next

            a.next = b.next
            b.next = a
            head = b
            a = a.next
            b=b.next
            b.next=self.swapPairs(a)

            return head

if __name__=="__main__":
    ls=[1,2,3,4]
    head=ListNode()
    head.create_a_linked_list_from_list(ls)
    A=Solution()
    b=A.swapPairs(head)
    b.show()