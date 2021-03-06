class Node:
    def __init__(self, char, len_prefix, is_end=False):
        self.char = char
        self.is_end = is_end
        self.len_prefix = len_prefix
        self.children = {}

class Trie:
    def __init__(self):
        self.root = Node("", 0)

    def add_word(self, word):
        self._add_word(self.root, word)

    def _add_word(self, root, word):
        if not word:
            return
        node = root.children.get(word[0])
        if not node:
            node = Node(word[0], root.len_prefix+1)
            root.children[word[0]] = node

        if len(word) > 1:
            self._add_word(node, word[1:])
        else:
            node.is_end = True

    def get_max_path_length_sum(self):
        self.res = 0
        self._dfs(self.root)
        return self.res

    def _dfs(self, root):
        if not root:
            return
        if root.is_end and not root.children:
            self.res += root.len_prefix + 1
            return

        for node in root.children.values():
            self._dfs(node)


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = Trie()
        for word in words:
            trie.add_word(word[::-1])
        return trie.get_max_path_length_sum()

