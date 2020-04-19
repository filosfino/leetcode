#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#
# https://leetcode-cn.com/problems/largest-number/description/
#
# algorithms
# Medium (35.96%)
# Likes:    268
# Dislikes: 0
# Total Accepted:    27.6K
# Total Submissions: 76.6K
# Testcase Example:  '[10,2]'
#
# 给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。
#
# 示例 1:
#
# 输入: [10,2]
# 输出: 210
#
# 示例 2:
#
# 输入: [3,30,34,5,9]
# 输出: 9534330
#
# 说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。
#
#

# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not nums:
            return ''
        class StringNumber(str):
            def __lt__(self, y):
                return self + y < y + self

        ret = sorted(map(str, nums), key=StringNumber)[::-1]
        ret = "".join(ret)
        return ret.lstrip('0') or '0'


# @lc code=end
