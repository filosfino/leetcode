#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#
# https://leetcode.cn/problems/permutation-in-string/description/
#
# algorithms
# Medium (44.15%)
# Likes:    742
# Dislikes: 0
# Total Accepted:    214.6K
# Total Submissions: 486K
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# 给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。
#
# 换句话说，s1 的排列之一是 s2 的 子串 。
#
#
#
# 示例 1：
#
#
# 输入：s1 = "ab" s2 = "eidbaooo"
# 输出：true
# 解释：s2 包含 s1 的排列之一 ("ba").
#
#
# 示例 2：
#
#
# 输入：s1= "ab" s2 = "eidboaoo"
# 输出：false
#
#
#
#
# 提示：
#
#
# 1 <= s1.length, s2.length <= 10^4
# s1 和 s2 仅包含小写字母
#
#
#

# @lc code=start
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ls1 = len(s1)
        ls2 = len(s2)
        if ls2 < ls1:
            return False

        tgt = Counter(s1)
        for i in range(0, ls2 - ls1 + 1):
            if Counter(s2[i : i + ls1]) == tgt:
                return True
        return False


# @lc code=end


# s1
# [1,2]
# s2
# [1,2,3]
