# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def max_abs(self, val, root):
        if root.left == None and root.right == None:
            return abs(val - root.val)
        elif root.left != None and root.right == None:
            return max(abs(val - root.val), self.max_abs(val, root.left))
        elif root.right != None and root.left == None:
            return max(abs(val - root.val), self.max_abs(val, root.right))
        else:
            a=self.max_abs(val, root.right)
            b=self.max_abs(val, root.left)
            return max(abs(val - root.val), a, b)

    def maxAncestorDiff(self, root) -> int:
        if root == None or (root.left==None and root.right==None):
            return 0
        elif root.left == None and root.right != None:
            max_abs = self.max_abs(root.val, root.right)
            right_abs = self.maxAncestorDiff(root.right)
            if max_abs > right_abs:
                return max_abs
            else:
                return right_abs
        elif root.right == None and root.left != None:
            max_abs = self.max_abs(root.val, root.left)
            left_abs = self.maxAncestorDiff(root.left)
            if max_abs > left_abs:
                return max_abs
            else:
                return left_abs
        else:
            max_abs1 = self.max_abs(root.val, root.left)
            max_abs2 = self.max_abs(root.val, root.right)
            left_abs = self.maxAncestorDiff(root.left)
            right_abs = self.maxAncestorDiff(root.right)
            return max(max_abs1, max_abs2, left_abs, right_abs)

if __name__=="__main__":
    node8=TreeNode(8)
    node3=TreeNode(3)
    node10=TreeNode(10)
    node1 = TreeNode(1)
    node6 = TreeNode(6)
    node14 = TreeNode(14)
    node4 = TreeNode(4)
    node7 = TreeNode(7)
    node13 = TreeNode(13)

    node6.left=node4
    node6.right=node7

    node14.left=node13

    node3.left=node1
    node3.right=node6

    node10.right=node14

    node8.left=node3
    node8.right=node10

    a=Solution()
    b=a.maxAncestorDiff(node8)
    print(b)