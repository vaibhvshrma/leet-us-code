class AlienWord:
    def __init__(self, word, order):
        self.order = order
        self.mp = {char: idx for (idx, char) in enumerate(order)}
        self.word = word

    def __lt__(self, other):
        self_len, other_len = len(self.word), len(other.word)
        i = 0
        while i < self_len and i < other_len:
            s_ch, o_ch = self.word[i], other.word[i]
            if s_ch != o_ch:
                return self.mp.get(s_ch) < self.mp.get(o_ch)
            i += 1
        return self_len < other_len

    def __eq__(self, other):
        return self.word == other.word


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(1, len(words)):
            f, s = AlienWord(words[i-1], order), AlienWord(words[i], order)
            if not (f == s or f < s):
                return False
        return True
