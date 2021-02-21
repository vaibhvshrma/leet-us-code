class Solution:
    def helper(self, num, n, k):
        if len(num) == n:
            self.res.add(int(num))
            return
        last = int(num[-1])
        if last - k >= 0:
            self.helper(num + str(last-k), n, k)
        if last + k < 10:
            self.helper(num + str(last+k), n, k)
            
            
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        self.res = set()
        for i in range(1, 10):
            self.helper(str(i), n, k)
        return list(self.res)
