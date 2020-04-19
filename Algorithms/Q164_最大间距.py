#
# @lc app=leetcode.cn id=164 lang=python3
#
# [164] 最大间距
#
# https://leetcode-cn.com/problems/maximum-gap/description/
#
# algorithms
# Hard (54.88%)
# Likes:    138
# Dislikes: 0
# Total Accepted:    13.2K
# Total Submissions: 24K
# Testcase Example:  '[3,6,9,1]'
#
# 给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。
#
# 如果数组元素个数小于 2，则返回 0。
#
# 示例 1:
#
# 输入: [3,6,9,1]
# 输出: 3
# 解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。
#
# 示例 2:
#
# 输入: [10]
# 输出: 0
# 解释: 数组元素个数小于 2，因此返回 0。
#
# 说明:
#
#
# 你可以假设数组中所有元素都是非负整数，且数值在 32 位有符号整数范围内。
# 请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。
#
#
#
import math

# @lc code=start
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        max_v, min_v = max(nums), min(nums)
        gap = math.ceil((max_v - min_v) / (len(nums) - 1))
        if not gap:
            return 0
        buckets = [[] for i in range(len(nums))]
        for num in nums:
            buckets[int((num - min_v) // gap)].append(num)
        buckets = [(min(bucket), max(bucket)) for bucket in buckets if bucket]
        maxGap = 0
        prev_bucket_max = None
        for bucket in buckets:
            if prev_bucket_max is not None:
                maxGap = max(bucket[0] - prev_bucket_max, maxGap)
            prev_bucket_max = bucket[1]
        return maxGap


# @lc code=end
