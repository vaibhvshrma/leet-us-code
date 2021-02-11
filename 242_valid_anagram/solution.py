from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = Counter(s)
        t_count = Counter(t)
        if len(s_count) != len(t_count):
            return False

        for char in s_count:
            if s_count[char] != t_count[char]:
                return False

        return True
