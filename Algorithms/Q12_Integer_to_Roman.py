# -- coding: utf-8 --
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ret = []
        div, mod = divmod(num, 1000)
        ret.extend(['M'*div])

        div, mod = divmod(mod, 100)
        if div == 9:
            ret.extend(['CM'])
        elif div == 4:
            ret.extend(['CD'])
        elif div >= 5:
            ret.append('D')
            ret.extend(['C'*(div-5)])
        else:
            ret.extend(['C'*div])

        div, mod = divmod(mod, 10)
        if div == 9:
            ret.extend(['XC'])
        elif div == 4:
            ret.extend(['XL'])
        elif div >= 5:
            ret.append('L')
            ret.extend(['X'*(div-5)])
        else:
            ret.extend(['X'*div])

        if mod == 9:
            ret.extend(['IX'])
        elif mod == 4:
            ret.extend(['IV'])
        elif mod >= 5:
            ret.append('V')
            ret.extend(['I'*(mod-5)])
        else:
            ret.extend(['I'*mod])
        return ''.join(ret)




