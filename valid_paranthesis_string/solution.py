from collections import deque, namedtuple

class Solution:
    def checkValidString(self, input_string: str) -> bool:
        par_count = ast_count = 0

        left_bracket_queue = deque()
        ast_queue = deque()

        for idx, char in enumerate(input_string):
            if char == '(':
                par_count += 1
                left_bracket_queue.append(idx)
            elif char == ')':
                par_count -= 1
                if left_bracket_queue:
                    left_bracket_queue.pop()
            else:
                ast_count += 1
                ast_queue.append(idx)

            if par_count < 0:
                if ast_count:
                    ast_count -= 1
                    ast_queue.popleft()
                else:
                    return False

        while left_bracket_queue and ast_queue:
            bracket_pos = left_bracket_queue.popleft()
            while ast_queue and ast_queue[0] <= bracket_pos:
                ast_queue.popleft()
            if ast_queue:
                # found a satisfying asterisk
                ast_queue.popleft()
            else:
                return False

        return not bool(left_bracket_queue)
