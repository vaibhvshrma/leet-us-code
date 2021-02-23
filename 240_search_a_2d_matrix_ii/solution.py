class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo, hi = 0, len(matrix[0])-1
        while lo < hi:
            mid = lo + ((hi-lo+1)//2)
            if matrix[0][mid] <= target:
                lo = mid
            else:
                hi = mid-1
        if matrix[0][lo] == target:
            return True
        if matrix[0][lo] > target:
            return False
        
        max_col = lo
        lo, hi = 0, len(matrix)-1
        while lo < hi:
            mid = lo + ((hi-lo+1)//2)
            if matrix[mid][0] <= target:
                lo = mid
            else:
                hi = mid-1
                
        max_row = lo
        for i in range(1, max_row+1):
            lo, hi = 0, len(matrix[0])-1
            while lo < hi:
                mid = lo + ((hi-lo+1)//2)
                if matrix[i][mid] <= target:
                    lo = mid
                else:
                    hi = mid-1
            if matrix[i][lo] == target:
                return True
            
        return False
