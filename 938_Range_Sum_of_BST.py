# Definition for a binary tree node.
class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def create_tree_from_list(self,ls):
        tree=None
        root=None
        for i in range(len(ls)):
            a=TreeNode(ls[i])
            if tree==None:
                tree=a
            else:
                pass




class Solution():
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        pass

if __name__=="__main__":
    pass

'''chua giai quyet duoc'''