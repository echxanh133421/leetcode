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
class Solution():
    def len(self,head):
        if head==None:
            return 0
        elif head.next==None:
            return 1
        else:
            l=1
            while head.next!=None:
                l+=1
                head=head.next
            return l
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        first=None
        a=head
        if head==None:
            return None
        elif head.next==None:
            return head
        else:
            for i in range(self.len(head)):
                while head.next!=None:
                    remember=head
                    head=head.next
                node = ListNode(head.val)
                remember.next = None
                if first == None:
                    first = node
                    head_return=first
                else:
                    first.next = node
                    first=first.next
                head=a
            return head_return




if __name__=="__main__":
    head = [1, 2, 3, 4, 5]
    ls=ListNode()
    ls.create_a_linked_list_from_list(head)
    A=Solution()
    # print(A.len(ls))
    b=A.reverseList(ls)
    b.show()

    '''chậm và tốn tài nguyên'''
