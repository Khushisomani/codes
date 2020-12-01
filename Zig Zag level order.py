# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        nxt_reverse = True
        
        queue = collections.deque()
        queue.append(root)
        res = []
        
        while queue:
            c=collections.deque()
            for i in range(len(queue)):
                a=queue.popleft()
                if nxt_reverse:
                    c.append(a.val)
                else:
                    c.appendleft(a.val)
                if a.left:
                    queue.append(a.left)
                if a.right:
                    queue.append(a.right)
            nxt_reverse=not nxt_reverse
            res.append(list(c))    
        return res
        