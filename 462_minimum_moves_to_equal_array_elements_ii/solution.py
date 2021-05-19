class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        common = sorted(nums)[(len(nums)//2)]
        res = sum([abs(num-common) for num in nums])
        return res
