# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]

        if not root:
            return res

        q=[]
        q.append(root)

        while q:
            n=len(q)
            r=None
            for i in range(n):
                cur=q.pop(0)
                if cur:
                    r=cur
                    q.append(cur.left)
                    q.append(cur.right)
            if r:
                res.append(r.val)
        return res