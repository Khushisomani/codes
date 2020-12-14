# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        v=[]
        while head:
            v.append(head.val)
            head=head.next
        def f(v):
            if not v:
                return None
            mid=len(v)//2
            node=TreeNode(v[mid])
            node.left=f(v[:mid])
            node.right=f(v[mid+1:])
            return node
        return f(v)
            
            
            
        
        
        