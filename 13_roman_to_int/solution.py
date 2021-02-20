class Solution:
    def romanToInt(self, s: str) -> int:
        val = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        res = val[s[0]]
        for i in range(1, len(s)):
            x, y = s[i-1], s[i]
            if val[x] < val[y]:
                res -= val[x] << 1
            res += val[y]
            
        return res
