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
    def len(self, head):
        if head==None:
            return 0
        elif head.next==None:
            return 1
        else:
            count=1
            while head.next!=None:
                count+=1
                head=head.next
            return count
    def merge(self,list1,list2):
        if list1 == None and list2 == None:
            return None
        elif list1 == None or list2 == None:
            if list1 == None:
                return list2
            else:
                return list1
        else:
            len_l1 = self.len(list1)
            len_l2 = self.len(list2)

            i = 1
            j = 1
            l3 = None
            head = l3
            while i <= len_l1 and j <= len_l2:
                l4 = ListNode()
                if l3 == None:
                    l3 = l4
                    head = l3
                else:
                    l3.next = l4
                    l3 = l3.next
                if list1.val <= list2.val:
                    l3.val = list1.val
                    list1 = list1.next
                    i += 1
                else:
                    l3.val = list2.val
                    list2 = list2.next
                    j += 1

            if list1 == None and list2 != None:
                l3.next = list2

            if list2 == None and list1 != None:
                l3.next = list1

            return head

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return head
        elif head.next==None:
            return head
        else:
            a=head
            a1=head
            len=int(self.len(head)/2)-1
            head=head.next
            while len:
                a1=a1.next
                head=head.next
                len-=1
            a1.next=None
            b=head
            a2=self.sortList(a)
            b2=self.sortList(b)
            c=self.merge(a2,b2)
            return c


if __name__=="__main__":
    head=[4,2,1,3]
    ls_node=ListNode()
    ls_node.create_a_linked_list_from_list(head)
    # print(id(ls_node))
    a=Solution()
    # b=a.len(ls_node)
    # print(b)
    b=a.sortList(ls_node)
    b.show()