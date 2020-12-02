# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder:
            x=inorder.index(postorder.pop())
            root=TreeNode(inorder[x])
            root.left=self.buildTree(inorder[:x],postorder[:x])
            root.right=self.buildTree(inorder[x+1:],postorder[x:])
            return root
            
        