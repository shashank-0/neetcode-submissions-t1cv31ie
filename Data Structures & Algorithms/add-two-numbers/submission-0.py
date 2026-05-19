# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def rec(n,cur):
            if not cur.next:
                return (10**n)*cur.val
            else:
                return rec(n+1,cur.next)+(10**n)*cur.val
        
        sum=rec(0,l1)+rec(0,l2)
        curr=None
        for i in str(sum):
            a=ListNode(int(i))
            a.next=curr
            curr=a
        
        return curr
