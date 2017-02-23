class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapping = {
            '{': '}',
            '(': ')',
            '[': ']',
        }
        opened = mapping.keys()
        closed = mapping.values()
        stack = []

        for i in s:
            if i in opened:
                stack.append(i)
            if i in closed:
                if len(stack) and mapping[stack.pop()] == i:
                    continue
                else:
                    return False
        return not bool(stack)
