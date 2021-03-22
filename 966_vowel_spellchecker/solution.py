class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = "aeiouAEIOU"
        table = str.maketrans({ v: '*' for v in vowels })
        words = set(wordlist)
        lcase_words = {}
        wo_vowels = {}
        for word in wordlist:
            lc_word = word.lower()
            tr_word = word.translate(table).lower()
            if lc_word not in lcase_words:
                lcase_words[lc_word] = word
            if tr_word not in wo_vowels:
                wo_vowels[tr_word] = word
        
        res = []
        for query in queries:
            tr_query = query.translate(table).lower()
            lc_query = query.lower()
            if query in words:
                ires = query
            elif lc_query in lcase_words:
                ires = lcase_words[lc_query]
            elif tr_query in wo_vowels:
                ires = wo_vowels[tr_query]
            else:
                ires = ""
            
            res.append(ires)

        return res
