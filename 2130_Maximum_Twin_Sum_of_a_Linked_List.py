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
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        ls=[]
        while head.next!=None:
            ls.append(head.val)
            head=head.next
        ls.append(head.val)

        max=ls[0]+ls[len(ls)-1]
        for i in range(1,int(len(ls)/2)):
            sum=ls[i]+ls[len(ls)-1-i]
            if sum>max:
                max=sum
        return max



if __name__=="__main__":
    ls=[5,4,2,1]
    head=ListNode()
    head.create_a_linked_list_from_list(ls)
    A=Solution()
    sum=A.pairSum(head)
    print(sum)
