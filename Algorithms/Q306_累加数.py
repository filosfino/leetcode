#
# @lc app=leetcode.cn id=306 lang=python3
#
# [306] 累加数
#
# https://leetcode.cn/problems/additive-number/description/
#
# algorithms
# Medium (38.16%)
# Likes:    374
# Dislikes: 0
# Total Accepted:    44.1K
# Total Submissions: 115.6K
# Testcase Example:  '"112358"'
#
# 累加数 是一个字符串，组成它的数字可以形成累加序列。
#
# 一个有效的 累加序列 必须 至少 包含 3 个数。除了最开始的两个数以外，序列中的每个后续数字必须是它之前两个数字之和。
#
# 给你一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是 累加数 。如果是，返回 true ；否则，返回 false 。
#
# 说明：累加序列里的数，除数字 0 之外，不会 以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。
#
#
#
# 示例 1：
#
#
# 输入："112358"
# 输出：true
# 解释：累加序列为: 1, 1, 2, 3, 5, 8 。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
#
#
# 示例 2：
#
#
# 输入："199100199"
# 输出：true
# 解释：累加序列为: 1, 99, 100, 199。1 + 99 = 100, 99 + 100 = 199
#
#
#
# 提示：
#
#
# 1 <= num.length <= 35
# num 仅由数字（0 - 9）组成
#
#
#
#
# 进阶：你计划如何处理由过大的整数输入导致的溢出?
#
#

# @lc code=start
class Solution:
    def validate(self, a: int, b: int, remaining: str) -> bool:
        print(f"validating {a=} {b=} {remaining}")
        vals = [a, b]
        while remaining:
            last_two_sum = vals[-1] + vals[-2]
            last_two_sum_str = str(last_two_sum)
            if not remaining.startswith(last_two_sum_str):
                return False
            remaining = remaining[len(last_two_sum_str) :]
            vals.append(last_two_sum)
        return True

    def isAdditiveNumber(self, num: str) -> bool:
        # 前两个数字决定了后面的序列，首先排列出所有可能性
        # 前两个数字的长度相加必定 < len(num)
        total_length = len(num)
        fst_start = 0
        for fst_end in range(0, total_length - 2):  # 至少预留两个数字位给 2th 3rd
            fst_num = int(num[fst_start : fst_end + 1])
            second_start = fst_end + 1
            for second_end in range(second_start, total_length - 1):  # 至少预留1个数字位给 3rd
                second_num = int(num[second_start : second_end + 1])
                if self.validate(fst_num, second_num, num[len(f"{fst_num}{second_num}") :]):
                    return True
        return False


# @lc code=end
