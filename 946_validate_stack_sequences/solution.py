class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        ptr = 0
        stack = []
        stack_elems = set()
        for pop in popped:
            if pop not in stack_elems:
                while ptr < len(pushed) and pop not in stack_elems:
                    push = pushed[ptr]
                    stack.append(push)
                    stack_elems.add(push)
                    ptr += 1
            
            if not stack or stack[-1] != pop:
                return False
            
            stack_elems.remove(stack.pop())
        
        return True                    
