class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length == 0:
            return 0

        current_index = length - 1
        last_char_index = None
        last_space_index_before_last_char = None

        while current_index >= 0:
            if s[current_index].isspace():
                if last_char_index is not None:
                    last_space_index_before_last_char = current_index
                    break
            else:
                if last_char_index is None:
                    last_char_index = current_index

            current_index -= 1

        if last_char_index is None:
            return 0
        elif last_space_index_before_last_char is None:
            return last_char_index + 1
        else:
            return last_char_index - last_space_index_before_last_char


