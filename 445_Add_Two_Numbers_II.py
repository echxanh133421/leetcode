
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

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1=0
        num2=0

        head=None
        while l1!=None:
            num1=num1*10+l1.val
            l1=l1.next
        while l2!=None:
            num2=num2*10+l2.val
            l2=l2.next

        sum=num1+num2
        lst=list(str(sum))
        for i in range(len(lst)):
            node=ListNode(int(lst[i]))
            if head==None:
                head=node
                first=head
            else:
                head.next=node
                head=head.next
        return first





if __name__=="__main__":
    l1 = [7, 2, 4, 3]
    l2 = [5, 6, 4]
    head1=ListNode()
    head1.create_a_linked_list_from_list(l1)
    head2=ListNode()
    head2.create_a_linked_list_from_list(l2)

    A=Solution()
    b=A.addTwoNumbers(head1,head2)
    # print(b)
    b.show()

