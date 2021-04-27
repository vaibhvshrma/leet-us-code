class Solution:
    @staticmethod
    def get_jumps(heights, end):
        jumps = []
        for i in range(1, end+1):
            diff = heights[i] - heights[i-1]
            if diff > 0:
                jumps.append(diff)
        return jumps

    @staticmethod
    def is_enough_bricks_and_ladders(jumps, bricks, ladders):
        if ladders >= len(jumps):
            return True
        jumps.sort(reverse=True)
        return sum(jumps[ladders:]) <= bricks

    def can_reach_building(self, i, heights, bricks, ladders):
        jumps = self.get_jumps(heights, i)
        return self.is_enough_bricks_and_ladders(jumps, bricks, ladders)

    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        lo, hi = 0, len(heights)-1

        while lo < hi:
            mid = lo + (hi-lo+1)//2
            if self.can_reach_building(mid, heights, bricks, ladders):
                lo = mid
            else:
                hi = mid-1
        return lo
