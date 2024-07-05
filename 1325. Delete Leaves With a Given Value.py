# Definition for a binary tree node.
import tarfile


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def removeLeafNodes(self, root, target: int):
        if root.left==None and root.right==None:
            if root.val==target:
                return None
            else:
                return root
        elif root.left!=None and root.right==None:
            root.left=self.removeLeafNodes(root.left,target)
            return root
        elif root.left==None and root.right!=None:
            root.right=self.removeLeafNodes(root.right,target)
            return root
        else:
            root.left=self.removeLeafNodes(root.left,target)
            root.right=self.removeLeafNodes(root.right,target)
            return root
if __name__=="__main__":
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.left.left=TreeNode(2)
    root.right=TreeNode(3)
    root.right.left=TreeNode(2)
    root.right.right=TreeNode(4)
    a=Solution()
    b=a.removeLeafNodes(root,2)
    '''sai'''
