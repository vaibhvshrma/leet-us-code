class Solution:
    @staticmethod
    def is_permutation(pattern: str, string: str) -> bool:
        dest_to_src = {}
        src_to_dest = {}

        for i in range(len(pattern)):
            src, dest = string[i], pattern[i]
            have_src = dest_to_src.get(dest, src)
            if have_src != src:
                return False
            have_dest = src_to_dest.get(src, dest)
            if have_dest != dest:
                return False
            dest_to_src[dest] = src
            src_to_dest[src] = dest

        return True

    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        return [word for word in words if self.is_permutation(pattern, word)]
