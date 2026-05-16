# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recur(curr,prev):
            if not curr:
                return prev
            else:
                tmp=curr.next
                curr.next=prev
            return recur(tmp,curr)
        return recur(head,None)