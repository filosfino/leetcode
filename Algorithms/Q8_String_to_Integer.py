# -- coding: utf-8 --

class Solution(object):

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        max_positive_value = 2**31-1
        min_negative_value = -2**31

        int_val = []
        starrted = False
        for char in str:
            if char.isspace():
                if starrted:
                    break
                else:
                    continue
            elif char in ['+', '-'] and not starrted:
                int_val.append(char)
                starrted = True
            elif char.isdigit():
                int_val.append(char)
                starrted = True
            else:
                break

        try:
            ret = int(''.join(int_val))
        except Exception:
            ret = 0

        if min_negative_value > ret:
            return min_negative_value
        elif ret > max_positive_value:
            return max_positive_value
        else:
            return ret
