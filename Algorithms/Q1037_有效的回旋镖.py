#
# @lc app=leetcode.cn id=1037 lang=python3
#
# [1037] 有效的回旋镖
#
# https://leetcode.cn/problems/valid-boomerang/description/
#
# algorithms
# Easy (49.15%)
# Likes:    95
# Dislikes: 0
# Total Accepted:    38.3K
# Total Submissions: 77.8K
# Testcase Example:  '[[1,1],[2,3],[3,2]]'
#
# 给定一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点，如果这些点构成一个 回旋镖 则返回 true
# 。
#
# 回旋镖 定义为一组三个点，这些点 各不相同 且 不在一条直线上 。
#
#
#
# 示例 1：
#
#
# 输入：points = [[1,1],[2,3],[3,2]]
# 输出：true
#
#
# 示例 2：
#
#
# 输入：points = [[1,1],[2,2],[3,3]]
# 输出：false
#
#
#
# 提示：
#
#
#
# points.length == 3
# points[i].length == 2
# 0 <= xi, yi <= 100
#
#
#

# @lc code=start
from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        # 两个条件
        # 1. 三个点不重叠
        # 2. 三个点不在同一直线上
        point_set = set(map(tuple, points))
        if len(point_set) != 3:
            return False
        a, b, c = points
        if (c[1] - b[1]) * (a[0] - b[0]) == (a[1] - b[1]) * (c[0] - b[0]):
            return False
        return True


# @lc code=end
