class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        l = r = -1
        if nums[0] == 0:
            l = r = 0
        elif nums[0] == 1:
            r = 0

        for i in range(1, len(nums)):
            if nums[i] == 0:
                nums[i] = nums[i-1]
                if r-l > 0:
                    nums[r+1] = nums[r]
                if l >= 0:
                    nums[l+1] = nums[l]
                else:
                    nums[0] = 0
                l += 1
                r += 1
            elif nums[i] == 1:
                nums[i] = nums[i-1]
                if r-l > 0 and r >= 0:
                    nums[r+1] = nums[r]
                else:
                    nums[r+1] = 1
                r += 1
            