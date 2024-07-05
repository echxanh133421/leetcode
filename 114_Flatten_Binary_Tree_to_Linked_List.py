# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root==None :
            pass
        elif root.left==None and root.right==None:
            pass
        else:
            if root.left==None and  root.right!=None:
                self.flatten(root.right)
            elif root.left!=None and root.right==None:
                root.right=root.left
                root.left = None
                self.flatten(root.right)
            else:
                #gan con phai vao hau due phai cung cua con trai
                #gan con trai vao con phai
                #flatten con phai
                #buoc1:
                head=root.left
                if head.right==None:
                    head.right=root.right
                else:
                    while head.right!=None:
                        head=head.right
                    head.right=root.right
                #buoc2:
                root.right=root.left
                root.left=None
                #buoc3:
                self.flatten(root.right)

if __name__=="__main__":
    #[1,2,5,3,4,null,6]
    #create tree test
    node3=TreeNode(3)
    node4=TreeNode(4)
    node2=TreeNode(2,node3,node4)
    node6=TreeNode(6)
    node5=TreeNode(5,None,node6)
    node1=TreeNode(1,node2,node5)
    A=Solution()
    A.flatten(node1)

