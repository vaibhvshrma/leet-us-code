class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        is_changed = False
        arr = nums[:]
        # try increasing a val
        for i in range(1, len(nums)):
            x, y = nums[i-1], nums[i]
            if x > y:
                if is_changed:
                    break
                nums[i] = x
                is_changed = True
        else:
            return True

        # try decreasing a val
        nums = arr
        is_changed = False
        for i in range(len(nums)-1, 0, -1):
            x, y = nums[i-1], nums[i]
            if x > y:
                if is_changed:
                    return False
                nums[i-1] = y
                is_changed = True

        return True
