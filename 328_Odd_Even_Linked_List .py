

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
    def oddEvenList(self, head) :
        odd=None
        even=None
        if head==None:
            return None
        elif head.next==None:
            return head
        else:
            i=1
            while head!=None:
                if i%2!=0:
                    node = ListNode(head.val)
                    if odd==None:
                        odd=node
                        head_odd=odd
                    else:
                        odd.next=node
                        odd=odd.next
                else:
                    node = ListNode(head.val)
                    if even == None:
                        even = node
                        head_even=even
                    else:
                        even.next = node
                        even = even.next
                head=head.next
                i+=1
            odd.next=head_even
            return head_odd





if __name__=="__main__":
    head = [2,1,3,5,6,4,7]
    ls=ListNode()
    ls.create_a_linked_list_from_list(head)
    A=Solution()
    b=A.oddEvenList(ls)
    b.show()