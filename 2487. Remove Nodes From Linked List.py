
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNodes(self, head):
        a = head
        ls = []
        while head.next != None:
            ls.append(head.val)
            head = head.next
        ls.append(head.val)
        #return ls


if __name__=="__main__":
    #head = [5,2,13,3,8]
    head=ListNode(5)
    head.next=ListNode(2)
    head.next.next = ListNode(13)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(8)
    a=Solution()
    b=a.removeNodes(head)
    print(b)
    '''chua giai quyet duoc'''