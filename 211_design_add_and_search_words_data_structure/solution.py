from collections import defaultdict
from typing import Dict

class Trie:
    @classmethod
    def add(cls, word: str, trie: Dict[str, Dict]):
        if len(word) < 1:
            trie["0"] = {}
            return

        curr_char = word[0]
        if curr_char not in trie:
            trie[curr_char] = defaultdict(dict)

        cls.add(word[1:], trie[curr_char])

    @classmethod
    def search(cls, word: str, trie: Dict[str, Dict]) -> bool:
        if not word:
            return trie and "0" in trie
        if not trie:
            return False
 
        curr_char = word[0]
        rem_word = word[1:]
        if curr_char == ".":
            return any([cls.search(rem_word, trie[char]) for char in trie.keys()])

        if curr_char not in trie:
            return False

        return cls.search(rem_word, trie[curr_char])



class WordDictionary:

    def __init__(self):
        self.trie = defaultdict(dict)

    def addWord(self, word: str) -> None:
        Trie.add(word, self.trie)

    def search(self, word: str) -> bool:
        return Trie.search(word, self.trie)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
