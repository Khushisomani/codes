# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        a=[]
        k=[]
        q=collections.deque([root])
        while q:
            for i in range(len(q)):
                s=q.popleft()
                a.append(s.val)
                if s.left:
                    q.append(s.left)
                if s.right:
                    q.append(s.right)
            k.append(a[-1])
                
        return k
            
        