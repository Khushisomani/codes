"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
		# level order traversal
        levels = [[root]]
        while levels:
            cur=levels.pop()
            nxt=[]
            prev=None
            for c in cur:
                if c.left:
                    nxt.append(c.left)
                if c.right:
                    nxt.append(c.right)
                if prev:
                    prev.next=c
                prev=c
            if nxt:
                levels.append(nxt)
        return root