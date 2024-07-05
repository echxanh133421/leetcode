# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def  len_list(self,head):
        if head==None:
            return 0
        elif head.next==None:
            return 1
        else:
            return 1+self.len_list(head.next)
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        len_ls=self.len_list(head)
        if len_ls==0:
            return None
        elif len_ls==1:
            return TreeNode(head.val)
        else:
            mid=int(len_ls/2)
            index=mid
            head_left=head
            while index!=0:
                head=head.next
                index-=1
            root=TreeNode(head.val)
            head=head.next
            root.right=self.sortedListToBST(head)
            a=head_left
            while mid!=1:
                a=a.next
                mid-=1
            a.next=None
            root.left = self.sortedListToBST(head_left)
            return root

if __name__=="__main__":
    head=ListNode(-10)
    head.next=ListNode(-3)
    node0=ListNode(0)
    head.next.next=node0
    head.next.next.next=ListNode(5)
    head.next.next.next.next =ListNode(9)

    a=Solution()
    b=a.sortedListToBST(head)
    print('hoan thanh')