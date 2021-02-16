class Solution:
    def helper(self, res, i):
        if i == len(self.S):
            self.res.append(res)
            return
        curr_char = self.S[i]
        if curr_char.isalpha():
            self.helper(res+curr_char.lower(), i+1)
            self.helper(res+curr_char.upper(), i+1)
        else:
            self.helper(res+curr_char, i+1)

    def letterCasePermutation(self, S: str) -> List[str]:
        self.res = []
        self.S = S
        self.helper("", 0)
        return self.res
