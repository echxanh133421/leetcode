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
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        a=head
        if head.next==None:
            pass
        else:
            ls_nums=[]
            while head.next!=None:
                ls_nums.append(head.val)
                head=head.next
            ls_nums.append(head.val)
            head=a
            if len(ls_nums)%2==0:
                l=len(ls_nums)/2
            else:
                l = int(len(ls_nums) / 2)+1

            for i in range(l):
                head.val=ls_nums[i]
                head=head.next
                if head==None:
                    break
                head.val=ls_nums[len(ls_nums)-i-1]
                head=head.next
                if head==None:
                    break
            head=a
if __name__=="__main__":
    ls=[1,2,3,4,5]
    a=ListNode()
    a.create_a_linked_list_from_list(ls)
    A=Solution()
    A.reorderList(a)
    a.show()