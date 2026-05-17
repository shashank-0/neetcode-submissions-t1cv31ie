# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length=0
        pointer=head
        while pointer:
            length+=1
            pointer=pointer.next
        target=length-n

        if target==0:
            return head.next
        
        pointer1=head
        for i in range(1,target):
            pointer1=pointer1.next
        if pointer1==head and not pointer1.next:
            return None
        pointer1.next=pointer1.next.next
        return head