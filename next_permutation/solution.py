class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        peak_idx = Solution.find_peak(nums)
        if peak_idx <= 0:
            return Solution.reverse(nums)
        replace_elem_idx = peak_idx-1
        nxt_greater_idx = Solution.find_next_greater(nums, nums[replace_elem_idx], start=peak_idx)
        Solution.swap(nums, replace_elem_idx, nxt_greater_idx)
        Solution.reverse(nums, start=peak_idx)
        
        
    @staticmethod
    def find_peak(arr):
        i = len(arr)-1
        while i > 0 and arr[i-1] >= arr[i]:
            i -= 1
        return i
    
    @staticmethod
    def reverse(arr, start=0, end=None):
        if end is None:
            end = len(arr)-1
        for i in range(((end-start)>>1)+1):
            Solution.swap(arr, start+i, end-i)
            
    @staticmethod
    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]
        
    @staticmethod
    def find_next_greater(arr, key, start=0, end=None):
        # reverse sorted array
        if end is None:
            end = len(arr)-1
        lo, hi = start, end
        
        while lo < hi:
            mid = lo + ((hi-lo+1)>>1)
            if arr[mid] > key:
                lo = mid
            else:
                hi = mid-1
        return lo
        
