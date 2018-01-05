# -- coding: utf-8 --


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ret = {}
        for s in strs:
            base = ''.join(sorted(s))
            if base in ret:
                ret[base].append(s)
            else:
                ret[base] = [s]
        return list(ret.values())

