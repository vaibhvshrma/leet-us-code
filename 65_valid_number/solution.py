class Solution:
    @staticmethod
    def is_integer(num: str) -> bool:
        if num[0] in ["+", "-"]:
            num = num[1:]
        return num.isdigit()

    @staticmethod
    def is_decimal(num: str) -> bool:
        if num[0] in ["+", "-"]:
            num = num[1:]
        if "." not in num:
            return False
        try:
            l, r = num.split(".")
        except:
            return False
        if not (l or r):
            return False
        if l and not Solution.is_integer(l):
            return False
        if r and not r.isdigit():
            return False
        return True

    def isNumber(self, s: str) -> bool:
        s = s.lower()
        if "e" not in s:
            return self.is_decimal(s) or self.is_integer(s)
        try:
            l, r = s.split("e")
        except:
            return False
        if not (l and r):
            return False
        return (self.is_decimal(l) or self.is_integer(l)) and self.is_integer(r)
