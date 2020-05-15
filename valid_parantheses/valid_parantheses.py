from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        opening = frozenset(list('{(['))
        opp = {
            '{': '}',
            '(': ')',
            '[': ']',
        }
        for p in s:
            if p in opening:
                stack.append(opp[p])
            else:
                if not stack or stack[-1] != p:
                    return False
                stack.pop()
                
        return not bool(stack)

if __name__ == "__main__":
    print(Solution().isValid(input()))