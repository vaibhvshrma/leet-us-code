class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        cnt = 0
        res = []
        for ch in s:
            res.append(ch)
            if ch == "(":
                cnt += 1
            if ch == ")":
                if cnt > 0:
                    cnt -= 1
                else:
                    res.pop()
                    
        s_arr = res[::-1]
        res = []
        cnt = 0
        for ch in s_arr:
            res.append(ch)
            if ch == ")":
                cnt += 1
            if ch == "(":
                if cnt > 0:
                    cnt -= 1
                else:
                    res.pop()
        
        return (''.join(reversed(res)))
