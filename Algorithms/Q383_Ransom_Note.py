# -- coding: utf-8 --
from collections import Counter, defaultdict


class Solution(object):
    # def canConstruct(self, ransomNote, magazine):
    #     """
    #     :type ransomNote: str
    #     :type magazine: str
    #     :rtype: bool
    #     """
    #     target = Counter(ransomNote)
    #     source = Counter(magazine)
    #     target_copy = target.copy()
    #     target.subtract(source)
    #     return all(map(lambda i: target[i]<=0, target_copy.keys()))

    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        source_dict = defaultdict(lambda: 0)
        for i in magazine:
            source_dict[i] += 1
        for i in ransomNote:
            if i in source_dict:
                source_dict[i] -= 1
                if source_dict[i] < 0:
                    return False
            else:
                return False
        return True
