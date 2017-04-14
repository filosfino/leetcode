# -- coding: utf-8 --


class Solution(object):

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        return self.read('1', n-1)

    def read(self, n, times):
        if times == 0:
            return n

        current_index = 0
        counting_num = None
        counting_count = 0
        ret = []

        while 1:
            if current_index >= len(n) or n[current_index] != counting_num:
                if counting_num is not None:
                    ret.append('%s%s' % (counting_count, counting_num))
                if current_index >= len(n):
                    break
                counting_num = n[current_index]
                counting_count = 1

            elif n[current_index] == counting_num:
                counting_count += 1

            current_index += 1

        ret = ''.join(ret)

        if times > 1:
            return self.read(ret, times-1)
        else:
            return ret


