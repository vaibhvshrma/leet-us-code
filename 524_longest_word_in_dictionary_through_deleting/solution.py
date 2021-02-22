class Solution:
    @staticmethod
    def is_subsequence(pattern, text):
        p_idx = 0
        for char in text:
            if pattern[p_idx] == char:
                p_idx += 1
            if p_idx == len(pattern):
                return True
        return False 
           
        
    def findLongestWord(self, s: str, d: List[str]) -> str:
        word_list = sorted(d, key=lambda x: (-len(x), x))
        for word in word_list:
            if Solution.is_subsequence(word, s):
                return word
        return ""
