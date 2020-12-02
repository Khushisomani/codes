# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else: # delete the root
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            pre=root
            leftest=root.right
            while leftest and leftest.left:
                pre=leftest
                leftest=leftest.left
            pre.val=leftest.val
            if pre==root:
                pre.right=leftest.right
            else:
                pre.left=leftest.right
        return root
                