# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head==None:
            return head
        else:
            prev=None
            temp=head
            while m>1:
                prev=temp
                temp=temp.next
                m-=1
                n-=1
            conn=prev
            curr=temp
            while n>0:
                next_node=temp.next
                temp.next=prev
                prev=temp
                temp=next_node
                n-=1
            if conn!=None:
                conn.next=prev
            else:
                head=prev
            curr.next=temp
            return head
            
        
        
        
        
        
        
        
        