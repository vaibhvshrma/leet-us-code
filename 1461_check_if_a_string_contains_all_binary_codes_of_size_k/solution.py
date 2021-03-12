class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen = set()
        sm = int(s[:k], 2)
        seen.add(sm)
        for i in range(k, len(s)):
            sm &= ((1<<(k-1))-1)
            sm <<= 1
            sm += s[i] == "1"
            seen.add(sm)
            if len(seen) == (1<<k):
                return True
        
        return False
