class Solution:
    """
    Idea is to get y as close to x as quickly as possible
    This means that we should halve y whenever we can
    """
    def brokenCalc(self, x: int, y: int) -> int:
        if x >= y:
            return x-y
        return 1 + (self.brokenCalc(x, y+1) if y & 1 else self.brokenCalc(x, y>>1))
