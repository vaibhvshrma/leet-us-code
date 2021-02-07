class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        res = []
        inf = 2 * len(s) + 1

        last_pos = -inf
        for i in range(len(s)):
            if s[i] == c:
                last_pos = i
            res.append(i - last_pos)

        last_pos = inf
        for i in range(len(s) - 1, -1, -1):
            if s[i] == c:
                last_pos = i
            res[i] = min(res[i], last_pos - i)

        return res
