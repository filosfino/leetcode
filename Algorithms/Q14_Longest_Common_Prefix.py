class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''

        pos = 0
        while 1:
            for string in strs:
                try:
                    if string[pos] == strs[0][pos]:
                        continue
                    else:
                        return strs[0][:pos]
                except IndexError:
                    return strs[0][:pos]
            pos += 1

