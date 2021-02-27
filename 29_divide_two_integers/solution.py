class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        neg = 1
        if dividend < 0:
            neg *= -1
        if divisor < 0:
            neg *= -1
                
        res = 0
        if divisor == -1 and dividend == -(1<<31):
            return (1<<31)-1
        if abs(divisor) == 1:
            return neg*abs(dividend)
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            dividend -= divisor
            res += 1
        res *= neg
        return res
