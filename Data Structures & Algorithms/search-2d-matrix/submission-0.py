class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i=0
        c=len(matrix[0])
        j=len(matrix)*c-1
        while(i<=j):
            m=(i+j+1)//2
            if target>matrix[m//c][m%c]:
                i=m+1
            elif target<matrix[m//c][m%c]:
                j=m-1
            else:
                return True
        return False