#
# @lc app=leetcode.cn id=526 lang=python3
#
# [526] 优美的排列
#
# https://leetcode.cn/problems/beautiful-arrangement/description/
#
# algorithms
# Medium (73.36%)
# Likes:    317
# Dislikes: 0
# Total Accepted:    41.1K
# Total Submissions: 56K
# Testcase Example:  '2'
#
# 假设有从 1 到 n 的 n 个整数。用这些整数构造一个数组 perm（下标从 1 开始），只要满足下述条件 之一 ，该数组就是一个 优美的排列
# ：
#
#
# perm[i] 能够被 i 整除
# i 能够被 perm[i] 整除
#
#
# 给你一个整数 n ，返回可以构造的 优美排列 的 数量 。
#
#
#
# 示例 1：
#
#
# 输入：n = 2
# 输出：2
# 解释：
# 第 1 个优美的排列是 [1,2]：
# ⁠   - perm[1] = 1 能被 i = 1 整除
# ⁠   - perm[2] = 2 能被 i = 2 整除
# 第 2 个优美的排列是 [2,1]:
# ⁠   - perm[1] = 2 能被 i = 1 整除
# ⁠   - i = 2 能被 perm[2] = 1 整除
#
#
# 示例 2：
#
#
# 输入：n = 1
# 输出：1
#
#
#
#
# 提示：
#
#
# 1 <= n <= 15
#
#
#

# @lc code=start
from collections import defaultdict


class Solution:
    def countArrangement(self, n: int) -> int:
        def is_val_valid_at_index(val: int, index: int):
            # perm[i] 能够被 i 整除
            # i 能够被 perm[i] 整除
            return (val % index == 0) or (index % val == 0)

        match = defaultdict(list)
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if is_val_valid_at_index(j, i):
                    match[i].append(j)

        # print(match)
        ret = 0
        numbers_used = set()

        def backtrack(ith: int):
            if ith == n + 1:
                nonlocal ret
                ret += 1
                return

            # 放第 i 个位置的数字
            for picked in match[ith]:
                if picked in numbers_used:
                    continue
                numbers_used.add(picked)
                backtrack(ith + 1)
                numbers_used.discard(picked)

        backtrack(1)
        return ret


# @lc code=end
