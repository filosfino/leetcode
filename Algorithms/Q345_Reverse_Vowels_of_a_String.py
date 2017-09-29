# -- coding: utf-8 --

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        lower_vowels = ['a', 'e', 'i', 'o', 'u']
        upper_vowels = [i.upper() for i in lower_vowels]
        vowels = lower_vowels + upper_vowels

        s = list(s)
        i = 0
        matched_vowels = []
        while i < len(s):
            if s[i] in vowels:
                matched_vowels.append(i)
            i += 1
        if matched_vowels:
            j = 0
            while j <= (len(matched_vowels)-1)//2:
                s[matched_vowels[j]], s[matched_vowels[-j-1]] = s[matched_vowels[-j-1]], s[matched_vowels[j]]
                j += 1
        return ''.join(s)

