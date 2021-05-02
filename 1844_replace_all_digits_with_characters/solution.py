class Solution:
    def replaceDigits(self, s: str) -> str:
        alphabet = [chr(ord('a')+i) for i in range(26)]
        s_mod = list(s)

        for i in range(1, len(s), 2):
            c = s[i-1]
            s_mod[i] = alphabet[ord(c)+int(s[i])-ord('a')]

        return ''.join(s_mod)
