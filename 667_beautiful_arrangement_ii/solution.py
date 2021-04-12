class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        res = [1]
        last = 1
        sign = 1
        for i in range(k, 0, -1):
            curr = last + (sign*i)
            res.append(curr)
            last, sign = curr, -sign
        res.extend(i for i in range(k+2, n+1))
            
        return res
