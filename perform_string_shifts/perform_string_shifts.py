from typing import List

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        left = sum(map(lambda x: x[1], filter(lambda y: y[0] == 0, shift)))
        right = sum(map(lambda x: x[1], filter(lambda y: y[0] == 1, shift)))

        amt = abs(left-right)

        amt %= len(s)

        if not amt:
            return s

        if left > right:
            res = s[amt:] + s[:amt]
        else:
            res = s[:-amt] + s[-amt:]

        return res

if __name__ == '__main__':
    s = input()
    t = int(input())
    shift = [list(map(int, input().split())) for i in range(t)]

    print(Solution().stringShift(s, shift))
