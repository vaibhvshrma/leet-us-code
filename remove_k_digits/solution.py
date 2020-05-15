class Solution:
    def return_sol(self, res):
        i = 0
        while i < len(res) and res[i] == '0':
            i += 1
        s = res[i:]
        return ''.join(s) if s else '0'
    
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k:
            return '0'
        if not k:
            return num
        
        num = list(num)
        p = k
        stack = []
        
        for i in range(len(num)):
            while p and stack and stack[-1] > num[i]:
                stack.pop()
                p -= 1
            stack.append(num[i])
            
        return self.return_sol(stack[:len(num)-k])    





