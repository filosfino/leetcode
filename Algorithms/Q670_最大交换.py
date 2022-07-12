#
# @lc app=leetcode.cn id=670 lang=python3
#
# [670] 最大交换
#
# https://leetcode.cn/problems/maximum-swap/description/
#
# algorithms
# Medium (46.13%)
# Likes:    247
# Dislikes: 0
# Total Accepted:    27.7K
# Total Submissions: 60K
# Testcase Example:  '2736'
#
# 给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。
#
# 示例 1 :
#
#
# 输入: 2736
# 输出: 7236
# 解释: 交换数字2和数字7。
#
#
# 示例 2 :
#
#
# 输入: 9973
# 输出: 9973
# 解释: 不需要交换。
#
#
# 注意:
#
#
# 给定数字的范围是 [0, 10^8]
#
#
#

# @lc code=start
from collections import defaultdict


class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        拆分成单个数字从大到小排, 找出第一个置换位置并输出
        """
        chars = list(str(num))
        sorted_chars = sorted(chars, reverse=True)
        # print(f"{sorted_chars=}")
        # 放入最大数字
        swap_positions = []
        swap_values = []
        for big_i, (sorted_ch, ch) in enumerate(zip(sorted_chars, chars)):
            if sorted_ch != ch:
                swap_positions.append(big_i)  # big_i 是大值要放的位置, 也是小值当前的位置, 需要另外找出小值要放的位置，即大值的当前位置
                swap_values.extend([sorted_ch, ch])  # sorted_ch 是大值，ch 是小值
                break
        else:
            return num
        # print(f"{swap_positions=}")
        # print(f"{swap_values=}")
        # 找出置换位置
        big_val_max_i = -1
        for i, ch in enumerate(chars):
            if ch == swap_values[0] and i > swap_positions[0] and i > big_val_max_i:
                big_val_max_i = i
        swap_positions.append(big_val_max_i)
        # print(f"{swap_positions=}")
        # print(f"{swap_values=}")
        return int(
            "".join(
                [
                    *chars[: swap_positions[0]],
                    swap_values[0],
                    *chars[swap_positions[0] + 1 : swap_positions[1]],
                    swap_values[1],
                    *chars[swap_positions[1] + 1 :],
                ]
            )
        )


# @lc code=end
