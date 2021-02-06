from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pattern = {chr(x+ord('a')): 0 for x in range(26)}
        pattern.update(Counter(p))
        window = {chr(x+ord('a')): 0 for x in range(26)}
        window.update(Counter(s[:len(p)]))
        res = [0] if pattern == window else []

        for i in range(1, len(s)-len(p)+1):
            rem = s[i-1]
            ad = s[i+len(p)-1]
            if rem != ad:
                window[rem] -= 1
                window[ad] += 1
            if window == pattern:
                res.append(i)

        return res
