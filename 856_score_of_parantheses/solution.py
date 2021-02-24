class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        res = 0
        cnt = 0
        for i, c in enumerate(S):
            if c == '(':
                cnt += 1 
            else:
                cnt -= 1
                if S[i-1] == '(':
                    res += 1 << cnt
        return res
