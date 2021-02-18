class Solution:
    @staticmethod
    def numSlices(length):
        sumFirstN = lambda n: (n*(n+1)) >> 1
        return sumFirstN(length-2)
        
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        currLen = 0
        res = 0
        for i in range(2, len(A)):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                currLen += 1
            else:
                res += Solution.numSlices(currLen+2)
                currLen = 0
        return res + Solution.numSlices(currLen+2)
