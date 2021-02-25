class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        n = len(nums)
        l, r = 0, -1
        for i in range(n):
            if nums[i] != nums_sorted[i]:
                l = i
                break
        for i in range(n-1,-1,-1):
            if nums[i] != nums_sorted[i]:
                r = i
                break
        return r-l+1
