from typing import List

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        MOD = int(1e9)+7
        hcs = [0] + horizontalCuts + [h]
        vcs = [0] + verticalCuts + [w]
        hcs.sort()
        vcs.sort()

        max_diff_vert = max_diff_horz = 0

        for i in range(1, len(hcs)):
            x, y = hcs[i-1], hcs[i]
            max_diff_horz = max(max_diff_horz, y-x)

        for i in range(1, len(vcs)):
            x, y = vcs[i-1], vcs[i]
            max_diff_vert = max(max_diff_vert, y-x)

        return max_diff_horz * max_diff_vert % MOD
