class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root, val: int) :
        if root==None:
            return None
        else:
            if root.val==val:
                return root
            else:
                left=self.searchBST(root.left,val)
                if left!=None:
                    return left
                else:
                    return self.searchBST(root.right,val)

if __name__=="__main__":
    head4=TreeNode(4)
    head2=TreeNode(2)
    head7=TreeNode(7)
    head1=TreeNode(1)
    head3=TreeNode(3)
    head2.left=head1
    head2.right=head3
    head4.left=head2
    head4.right=head7
    a=Solution()
    b=a.searchBST(head4,2)
    print('giai duoc')