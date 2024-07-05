# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def have_one(self, root):
        if root == None:
            return False
        elif root.val == 1:
            return True
        else:
            return self.have_one(root.left) or self.have_one(root.right)

    def pruneTree(self, root) :
        if root.left == None and root.right == None:
            if root.val == 0:
                return None
            return root
        else:

            root_final = TreeNode(root.val)
            if root.val == 0:
                if self.have_one(root.left)==False and self.have_one(root.left) == False:
                    return None
                else:
                    if self.have_one(root.left):
                        root_final.left = self.pruneTree(root.left)
                    if self.have_one(root.right):
                        root_final.right = self.pruneTree(root.right)
                    return root_final
            else:
                if root.left == None and root.right != None:
                    if self.have_one(root.right):
                        root_final.right = self.pruneTree(root.right)
                    return root_final
                elif root.left != None and root.right == None:
                    if self.have_one(root.left):
                        root_final.left = self.pruneTree(root.left)
                    return root_final
                else:
                    if self.have_one(root.right):
                        root_final.right = self.pruneTree(root.right)
                    if self.have_one(root.left):
                        root_final.left = self.pruneTree(root.left)
                    return root_final

if __name__=="__main__":
    node1=TreeNode(1)
    node2=TreeNode(0)
    node3=TreeNode(0)
    node4=TreeNode(1)

    node2.left=node3
    node2.right=node4
    node1.right=node2

    a=Solution()
    b=a.pruneTree(node1)
