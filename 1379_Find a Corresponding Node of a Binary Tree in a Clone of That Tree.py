# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original==None:
            return None
        elif target.val==original.val:
            return cloned
        else:
            c = self.getTargetCopy(original.left, cloned.left, target)
            f = self.getTargetCopy(original.right,cloned.right,target)

            if c==None and f==None:
                return None
            elif c!=None:
                return c
            else:
                return f

if __name__=="__main__":
    head=TreeNode(7)
    head4=TreeNode(4)
    head3=TreeNode(3)
    head.left=head4
    head.right=head3
    head3.left=TreeNode(6)
    head3.right=TreeNode(19)

    head2 = TreeNode(7)
    head42 = TreeNode(4)
    head32 = TreeNode(3)
    head2.left = head42
    head2.right = head32
    head32.left = TreeNode(6)
    head32.right = TreeNode(19)

    node=TreeNode(3)
    a=Solution()
    b=a.getTargetCopy(head,head2,node)
    print(b.val)
