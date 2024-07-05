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
    def mergeInBetween(self, list1, a: int, b: int, list2):
        '''
        :param list1: ListNode
        :param a:  start index remove (int)
        :param b:  end index remove   (int)
        :param list2: ListNode insert
        :return: ListNode
        '''
        ls_result=list1
        head_ls1=list1
        head_ls2=list2
        while b:
            list1=list1.next
            b-=1
        while list2.next!=None:
            list2=list2.next
        list2.next=list1.next
        while a:
            remeber=head_ls1
            head_ls1=head_ls1.next
            a-=1
        remeber.next=head_ls2
        return ls_result






if __name__=="__main__":
    list1 = [0, 1, 2, 3, 4, 5]
    a = 3
    b = 4
    list2 = [1000000, 1000001, 1000002]
    ls1=ListNode()
    ls1.create_a_linked_list_from_list(list1)
    ls2=ListNode()
    ls2.create_a_linked_list_from_list(list2)


    A=Solution()
    B=A.mergeInBetween(ls1,a,b,ls2)
    B.show()
