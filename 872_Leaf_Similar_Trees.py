
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sequence_leaf(self,root):
        if root.left==None and root.right==None:
            return [root.val]
        elif root.left!=None and root.right==None:
            ls=[]
            ls+=self.sequence_leaf(root.left)
            return ls
        elif root.right!=None and root.left==None:
            ls=[]
            ls+=self.sequence_leaf(root.right)
            return ls
        else:
            ls=[]
            ls+=self.sequence_leaf(root.left)
            ls+=self.sequence_leaf(root.right)
            return ls

    def leafSimilar(self, root1, root2) -> bool:
        root1_sequence=self.sequence_leaf(root1)
        root2_sequence=self.sequence_leaf(root2)
        if len(root1_sequence)!=len(root2_sequence):
            return False
        else:
            for i in range(len(root1_sequence)):
                if root1_sequence[i]!=root2_sequence[i]:
                    return False
            return True