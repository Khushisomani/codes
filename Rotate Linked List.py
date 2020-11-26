# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        temp=head
        c=0
        while temp!=None:
            c+=1
            temp=temp.next
        if c!=0:
            k=k%c
        if k==0 or c==0:
            return head
        else:
            temp=head
            k=c-k
            while k>1:
                temp=temp.next
                k-=1
            knode=temp
            while temp.next!=None:
                temp=temp.next
            temp.next=head
            head=knode.next
            knode.next=None
            return head
        