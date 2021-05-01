class TrieNode:
    def __init__(self, letter=None, end=False):
        self.letter = letter
        self.end = end
        self.nbrs = {}
        self.indices = set()

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str, idx: int) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.nbrs:
                curr.nbrs[ch] = TrieNode(ch)
            curr = curr.nbrs[ch]
            curr.indices.add(idx)
        curr.end = True

    def startswith(self, prefix: str) -> Set[int]:
        curr = self.root
        for ch in prefix:
            curr = curr.nbrs.get(ch)
            if not curr:
                return set()
        return curr.indices

#     def find_all_complete_words_in_subtrie(self, root, word) -> List[str]:
#         res = []
#         if root.end:
#             res.append(word + root.letter)

#         for node in root.nbrs.values():
#             res.extend(self.find_all_complete_words_in_subtrie(node, word + root.letter))

#         return res


class WordFilter:

    def __init__(self, words: List[str]):
        word_map = {word: idx for idx, word in enumerate(words)}
        self.pref_trie = Trie()
        self.suff_trie = Trie()
        for word in words:
            idx = word_map.get(word)
            self.pref_trie.add_word(word, idx)
            self.suff_trie.add_word(word[::-1], idx)

    # def find_largest_index(self, target_words):
    #     for i in range(len(self.words)-1,-1,-1):
    #         if self.words[i] in target_words:
    #             return i

    def f(self, prefix: str, suffix: str) -> int:
        pref_match = self.pref_trie.startswith(prefix)
        suff_match = self.suff_trie.startswith(suffix[::-1])
        # suff_match = list(map(lambda x: x[::-1], suff_match))
        # res = set(pref_match) & set(suff_match)
        res = pref_match & suff_match
        if not res:
            return -1
        # if len(res) == 1:
        #     return len(self.words) - self.words[::-1].index(res.pop()) - 1
        # return self.find_largest_index(res)
        return max(res)

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
