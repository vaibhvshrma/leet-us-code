class Solution:
    def maxProduct(self, words: List[str]) -> int:
        res = 0
        word_letters_map = {word: set(word) for word in words}

        for i in range(len(words)):
            for j in range(i+1, len(words)):
                x, y = words[i], words[j]
                if not word_letters_map[x] & word_letters_map[y]:
                    res = max(res, len(x)*len(y))

        return res
