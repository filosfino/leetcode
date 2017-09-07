# -- coding: utf-8 --

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapping = {}
        for ss, tt in zip(s, t):
            if ss not in mapping:
                mapping[ss] = tt
            elif mapping[ss] != tt:
                return False
        if len(set(mapping.values())) != len(mapping):
            return False
        return True
