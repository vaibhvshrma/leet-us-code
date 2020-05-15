class Node:
    def __init__(self):
        # self.val = val
        self.next_map = {}
        self.word_ends_here = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr_node = self.root
        for c in word:
            if c not in curr_node.next_map:
                curr_node.next_map[c] = Node()
            curr_node = curr_node.next_map[c]

        curr_node.word_ends_here = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr_node = self.root
        for c in word:
            if c not in curr_node.next_map:
                return False
            curr_node = curr_node.next_map[c]

        return curr_node.word_ends_here

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr_node = self.root
        for c in prefix:
            if c not in curr_node.next_map:
                return False
            curr_node = curr_node.next_map[c]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)