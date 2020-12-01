# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        a=[]
        def inorder(root):
            if root:
                inorder(root.left)
                a.append(root.val)
                inorder(root.right)
            return a
        a=inorder(root)
        return a[k-1]
        