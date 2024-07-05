# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        sum=0
        if root.left==None and root.right==None:
            return 0
        elif root.left!=None and root.right==None:
            if root.left.left==None and root.left.right==None:
                return root.left.val
            else:
                sum+=self.sumOfLeftLeaves(root.left)
        elif root.right!=None and root.left==None:
            sum+=self.sumOfLeftLeaves(root.right)
        else:
            sum+=self.sumOfLeftLeaves(root.right)
            if root.left.left==None and root.left.right==None:
                sum+=root.left.val
            else:
                sum+=self.sumOfLeftLeaves(root.left)
        return sum

if __name__=="__main__":
    node3=TreeNode(3)
    node9=TreeNode(9)
    node20=TreeNode(20)
    node3.left=node9
    node3.right=node20

    node15=TreeNode(15)
    node7=TreeNode(7)
    node20.left=node15
    node20.right=node7

    A=Solution()
    b=A.sumOfLeftLeaves(node3)
    print(b)
