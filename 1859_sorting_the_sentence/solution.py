class Solution:
    def sortSentence(self, s: str) -> str:
        temp = s.split()
        temp.sort(key=lambda x: x[-1])
        return " ".join(map(lambda x: x[:-1], temp))
