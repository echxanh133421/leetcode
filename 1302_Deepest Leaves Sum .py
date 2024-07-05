import profile


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deep_tree(self,root):
        if root==None:
            return 0
        elif root.left==None and root.right==None:
            return 1
        else:
            deep_left=1+self.deep_tree(root.left)
            deep_right=1+self.deep_tree(root.right)
            if deep_left>deep_right:
                return deep_left
            else:
                return deep_right
    def get_item_deepest(self,root):
        ls=[]
        if root.left==None and root.right==None:
            return [root.val]
        else:
            if self.deep_tree((root.left))==self.deep_tree(root.right):
                ls+=self.get_item_deepest(root.left)+self.get_item_deepest(root.right)
            elif self.deep_tree((root.left))>=self.deep_tree(root.right):
                ls += self.get_item_deepest(root.left)
            else:
                ls += self.get_item_deepest(root.right)
            return ls


    def deepestLeavesSum(self, root) -> int:
        return sum(self.get_item_deepest(root))

if __name__=="__main__":
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.left.left=TreeNode(4)
    root.left.left.left=TreeNode(7)
    root.left.right=TreeNode(5)
    root.right=TreeNode(3)
    root.right.right=TreeNode(6)
    root.right.right.right=TreeNode(8)

    a=Solution()
    b=a.get_item_deepest(root)
    print(b)