class Solution:
    def rec_help(self, digits, word):
        if not digits:
            self.res.append(word)
            return
        rest_digits = digits[1:]
        for ch in self.mp.get(digits[0]):
            self.rec_help(rest_digits, word + ch)

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        self.mp = {
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        self.res = []
        self.rec_help(digits, "")
        return self.res
