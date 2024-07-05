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

    def nodesBetweenCriticalPoints(self, head) :
        if head ==None or head.next == None or head.next.next==None:
            return [-1,-1]
        else:
            ls=[]
            index=1
            a=head
            head=head.next
            while head.next!=None:
                if (head.val>a.val and head.val> head.next.val)or(head.val<a.val and head.val< head.next.val):
                    ls.append(index)
                index+=1
                head=head.next
                a=a.next
            if len(ls)<2:
                return [-1,-1]
            else:
                ls_result=[]
                min =ls[1]-ls[0]
                for i in range(1,len(ls)-1):
                    if ls[i+1]-ls[i]<min:
                        min=ls[i+1]-ls[i]
                ls_result.append(min)
                ls_result.append(ls[len(ls)-1]-ls[0])

                return ls_result

if __name__=="__main__":
    ls=[2,3,3,2]
    a=ListNode()
    a.create_a_linked_list_from_list(ls)
    A=Solution()
    b=A.nodesBetweenCriticalPoints(a)
    print(b)