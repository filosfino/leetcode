class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len1, len2 = len(num1), len(num2)
        len_max = len1 + len2
        ret = [0] * len_max

        num1, num2 = num1[::-1], num2[::-1]
        for i1, v1 in enumerate(num1):
            for i2, v2 in enumerate(num2):
                i = i1 + i2
                ret[i] = int(v1)*int(v2) + ret[i]
                # print(i1, v1, i2, v2, ret)
        # print(ret)
        for i in range(len_max):
            if ret[i] >= 10:
                carry, ret[i] = divmod(ret[i], 10)
                ret[i+1] += carry
                # print('processing %s: %s' %(i, ret))
        if not any(ret):
            # 全 0
            return '0'
        ret = ''.join([str(i) for i in ret[::-1]])
        return ret.lstrip('0')

