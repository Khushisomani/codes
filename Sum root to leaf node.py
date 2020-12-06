# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    48ms 14.21%
    14MB 46.21%
    """
    def sumNumbers(self, root: TreeNode) -> int:
        return self.helper(root,0)
    
    def helper(self,root,prev)->int:
        if not root:return 0
        temp=10*prev+root.val
        ans=0
        if root.left:ans+=self.helper(root.left,temp)
        if root.right:ans+=self.helper(root.right,temp)
        if ans>0:return ans
        else:return temp