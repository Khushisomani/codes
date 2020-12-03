# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def validate(root, upper, lower):
            if root is None:
                return True
            
            if root.val <= lower or root.val >= upper:
                return False
        
            l = validate(root.left, root.val, lower)
            r = validate(root.right, upper, root.val)
        
            return l and r
        
        
        return validate(root, float("inf"), float("-inf")) 
                
        
        