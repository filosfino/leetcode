#
# @lc app=leetcode.cn id=229 lang=python3
#
# [229] 多数元素 II
#
# https://leetcode.cn/problems/majority-element-ii/description/
#
# algorithms
# Medium (53.75%)
# Likes:    622
# Dislikes: 0
# Total Accepted:    85.4K
# Total Submissions: 158.8K
# Testcase Example:  '[3,2,3]'
#
# 给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。
#
#
#
# 示例 1：
#
#
# 输入：nums = [3,2,3]
# 输出：[3]
#
# 示例 2：
#
#
# 输入：nums = [1]
# 输出：[1]
#
#
# 示例 3：
#
#
# 输入：nums = [1,2]
# 输出：[1,2]
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9
#
#
#
#
# 进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1)的算法解决此问题。
#
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        return [k for k, v in c.items() if v > len(nums) / 3]


# @lc code=end
