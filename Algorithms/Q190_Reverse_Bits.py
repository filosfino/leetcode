# -- coding: utf-8 --

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binary_string = '{:0>32}'.format(bin(n)[2:])[::-1]
        return int(binary_string, base=2)

