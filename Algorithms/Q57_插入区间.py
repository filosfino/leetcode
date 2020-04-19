#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#
# https://leetcode-cn.com/problems/insert-interval/description/
#
# algorithms
# Hard (37.13%)
# Likes:    129
# Dislikes: 0
# Total Accepted:    20.2K
# Total Submissions: 54.3K
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# 给出一个无重叠的 ，按照区间起始端点排序的区间列表。
#
# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
#
# 示例 1:
#
# 输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出: [[1,5],[6,9]]
#
#
# 示例 2:
#
# 输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出: [[1,2],[3,10],[12,16]]
# 解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
#
#
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        merge_start_index = None
        merging_interval = []
        for i, interval in enumerate(intervals):
            # 不相交
            if interval[1] < newInterval[0]:
                continue
            # 相交
            elif interval[1] >= newInterval[0] >= interval[0] or newInterval[0] <= interval[0] <= newInterval[1]:
                if merge_start_index is None:
                    merge_start_index = i
                    merging_interval = [min(interval[0], newInterval[0]), max(newInterval[1], interval[1])]
                else:
                    merging_interval = [min(merging_interval[0], interval[0]), max(interval[1], merging_interval[1])]
            elif interval[0] < newInterval[0] and interval[1] > newInterval[1]:
                return intervals
            # 不相交或结束
            elif interval[0] > newInterval[1]:
                if merge_start_index is None:
                    return intervals[:i] + [newInterval] + intervals[i:]
                else:
                    return intervals[:merge_start_index] + [merging_interval] + intervals[i:]
        if merge_start_index is None:
            return intervals + [newInterval]
        else:
            return intervals[:merge_start_index] + [merging_interval]


# @lc code=end
