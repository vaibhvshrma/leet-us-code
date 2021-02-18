class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        get_water = lambda x, y: min(height[x], height[y]) * abs(y-x)
        res = 0
        while l < r:
            res = max(res, get_water(l, r))
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                if height[l+1] >= height[r-1]:
                    l += 1
                else:
                    r -= 1
        return res
