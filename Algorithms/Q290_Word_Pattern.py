# -- coding: utf-8 --

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        mapping = {}
        words = str.split()
        if len(pattern) != len(words) or len(set(pattern)) != len(set(words)):
            return False
        for char, word in zip(pattern, words):
            if mapping.setdefault(char, word) != word:
                return False
        return True



