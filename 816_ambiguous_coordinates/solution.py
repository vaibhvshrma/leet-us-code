class Solution:
    @staticmethod
    def get_valid_nums(num: str) -> List[str]:
        if len(num) == 1:
            return [num]
        res = []
        for i in range(1, len(num)):
            whole, decimal = num[:i], num[i:]
            if Solution.is_valid_num(whole, decimal):
                res.append(f"{whole}.{decimal}")
        if Solution.is_valid_num(num, ""):
            res.append(num)

        return res

    @staticmethod
    def is_valid_num(whole: str, decimal: str) -> bool:
        if not whole or (len(whole) > 1 and whole.startswith("0")):
            return False
        if decimal.endswith("0"):
            return False
        return True

    def ambiguousCoordinates(self, s: str) -> List[str]:
        s = s[1:-1]
        res = []
        for i in range(1, len(s)):
            left, right = s[:i], s[i:]
            for left_num in self.get_valid_nums(left):
                for right_num in self.get_valid_nums(right):
                    res.append(f"({left_num}, {right_num})")
        return res
