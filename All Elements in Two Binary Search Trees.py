# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        a=[]
        q=[root1]
        if q==[None]:
            s=[]
        else:
            while q:
                for i in range(len(q)):
                    s=q.pop()
                    a.append(s.val)
                    if s.left:
                        q.append(s.left)
                    if s.right:
                        q.append(s.right)
        q=[root2]
        if q==[None]:
            s=[]
        else:
            while q:
                for i in range(len(q)):
                    s=q.pop()
                    a.append(s.val)
                    if s.left:
                        q.append(s.left)
                    if s.right:
                        q.append(s.right)
        a.sort()
        return a
        
        