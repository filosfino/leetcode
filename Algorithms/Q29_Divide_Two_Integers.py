class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend > 0) is (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)

        result = 0
        sub, multi = divisor, 1
        while dividend >= divisor:
            if dividend >= sub:
                dividend -= sub
                result += multi
                sub <<= 1
                multi <<= 1
            else:
                sub >>= 1
                multi >>= 1
        result = result if positive else -result
        return min(max(-2147483648, result), 2147483647)
