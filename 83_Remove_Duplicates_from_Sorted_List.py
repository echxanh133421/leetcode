# Definition for singly-linked list.
class SLinkedList:
   def __init__(self):
      self.headval = None

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
    def deleteDuplicates(self, head) :
        pass


if __name__=="__main__":
    node1=ListNode()
    node1.create_a_linked_list_from_list([1,1,1,2,2])
    node1.remove_same_element()
    # A=Solution()
    # head=SLinkedList()
    # head.headval=node1
    # A.deleteDuplicates(head)
    node1.show()

