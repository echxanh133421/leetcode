class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNodes(self, head) :

        if head.next == None:
            return head
        else:
            a = head
            b=head
            while head.next != None:
                if head.next.val <= head.val:
                    head = head.next
                else:
                    if a.val < head.next.val:
                        head = head.next
                        a = head
                        b=head
                    else:
                        # xóa node
                        b.next = head.next
                        head = head.next
                        b=b.next

            return a

if __name__=="__main__":
    head=ListNode(5)
    head.next=ListNode(2)
    head.next.next=ListNode(13)
    head.next.next.next=ListNode(3)
    head.next.next.next.next=ListNode(8)

    a=Solution()
    b=a.removeNodes(head)
    print('chưa ra')