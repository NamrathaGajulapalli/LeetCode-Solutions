     
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        c=0
        while temp:
            c+=1
            temp=temp.next
        s=c-n
        if c==n:
            return head.next
        prev=head
        for i in range(s-1):
            prev=prev.next
        prev.next=prev.next.next
        return head    
    





