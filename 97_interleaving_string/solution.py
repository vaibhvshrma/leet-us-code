class Solution:
    @staticmethod
    @functools.cache
    def dp(i, j, z, A, B, target):
        if i >= len(A):
            return B[j:] == target[z:]
        if j >= len(B):
            return A[i:] == target[z:]
        if A[i] == target[z] and Solution.dp(i+1, j, z+1, A, B, target):
                return True
        if B[j] == target[z] and Solution.dp(i, j+1, z+1, A, B, target):
                return True
        return False

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        return self.dp(0, 0, 0, s1, s2, s3)
