#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#
# https://leetcode.cn/problems/longest-consecutive-sequence/description/
#
# algorithms
# Medium (55.15%)
# Likes:    1367
# Dislikes: 0
# Total Accepted:    306.9K
# Total Submissions: 556.6K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
#
# 请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
#
#
#
# 示例 1：
#
#
# 输入：nums = [100,4,200,1,3,2]
# 输出：4
# 解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
#
# 示例 2：
#
#
# 输入：nums = [0,3,7,2,5,8,4,6,0,1]
# 输出：9
#
#
#
#
# 提示：
#
#
# 0
# -10^9
#
#
#

# @lc code=start
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        lookup = {}  # 每个节点记录自身形成的最大区间最小值和最大值，对于一个区间来讲，只有边缘节点的区间会被更新，这样才能符合 O(n) 的要求

        ans = 0
        for num in nums:
            l = num - 1
            li = l in lookup
            r = num + 1
            ri = r in lookup

            if num in lookup:
                continue
            elif li and ri:
                ll = lookup[l][0]
                rr = lookup[r][1]
                lookup[ll] = (ll, rr)
                lookup[rr] = (ll, rr)
                lookup[num] = (ll, rr)
                round_ans = rr - ll + 1
            elif li:
                ll = lookup[l][0]
                rr = num
                lookup[num] = (ll, rr)
                lookup[ll] = (ll, rr)
                round_ans = rr - ll + 1
            elif ri:
                ll = num
                rr = lookup[r][1]
                lookup[num] = (ll, rr)
                lookup[rr] = (ll, rr)
                round_ans = rr - ll + 1
            else:
                lookup[num] = (num, num)
                round_ans = 1
            ans = max(round_ans, ans)
        return ans


# @lc code=end
