class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        l, r = 0, 1
        have_these = set([nums[0]])
        sm = res = nums[0]

        while r < len(nums):
            x = nums[r]
            while x in have_these:
                have_these.remove(nums[l])
                sm -= nums[l]
                l += 1
            have_these.add(x)
            sm += x
            res = max(res, sm)
            r += 1
        return res
