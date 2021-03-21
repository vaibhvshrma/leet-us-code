class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        target = sorted(str(N))
        val = 1
        for i in range(30):
            if sorted(str(val)) == target:
                return True
            val <<= 1
        return False
