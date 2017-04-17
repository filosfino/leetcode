class Solution(object):

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        carry = 0
        a_index = len(a) - 1
        b_index = len(b) - 1
        ret_value = ''

        while carry or a_index >= 0 or b_index >= 0:

            a_bit = b_bit = 0

            if a_index >= 0:
                a_bit = int(a[a_index])
                a_index -= 1

            if b_index >= 0:
                b_bit = int(b[b_index])
                b_index -= 1

            bit_sum = sum([carry, a_bit, b_bit])
            carry, bit = divmod(bit_sum, 2)
            ret_value = str(bit) + ret_value

        return ret_value




