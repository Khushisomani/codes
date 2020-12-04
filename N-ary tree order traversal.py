"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        m = []
        def solve(node, depth=0):
            if node:
                if len(m) > depth:
                    m[depth].append(node.val)
                else:
                    m.append([node.val])
                for ch in node.children:
                    solve(ch, depth+1)
        solve(root)
        return m
                