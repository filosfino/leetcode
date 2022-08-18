#
# @lc app=leetcode.cn id=1020 lang=python3
#
# [1020] 飞地的数量
#
# https://leetcode.cn/problems/number-of-enclaves/description/
#
# algorithms
# Medium (61.82%)
# Likes:    183
# Dislikes: 0
# Total Accepted:    48.5K
# Total Submissions: 78.5K
# Testcase Example:  '[[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]'
#
# 给你一个大小为 m x n 的二进制矩阵 grid ，其中 0 表示一个海洋单元格、1 表示一个陆地单元格。
#
# 一次 移动 是指从一个陆地单元格走到另一个相邻（上、下、左、右）的陆地单元格或跨过 grid 的边界。
#
# 返回网格中 无法 在任意次数的移动中离开网格边界的陆地单元格的数量。
#
#
#
# 示例 1：
#
#
# 输入：grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# 输出：3
# 解释：有三个 1 被 0 包围。一个 1 没有被包围，因为它在边界上。
#
#
# 示例 2：
#
#
# 输入：grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# 输出：0
# 解释：所有 1 都在边界上或可以到达边界。
#
#
#
#
# 提示：
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 500
# grid[i][j] 的值为 0 或 1
#
#
#

# @lc code=start
from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # 等价于不和 grid 边界连通的 island 格子数量
        # 所有 island - 和边界连通的数量
        # 和边界连通的 island 通过 connected 1 来标记
        m = len(grid)
        n = len(grid[0])
        total_island_count = 0

        def is_island(pos: tuple[int, int]) -> bool:
            return grid[pos[0]][pos[1]] == 1

        # 标记边界上的 island
        islands_on_edge = set()
        for i in range(m):
            for j in range(n):
                if is_island((i, j)):
                    total_island_count += 1
                    if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                        islands_on_edge.add((i, j))
        print(islands_on_edge)

        def get_island_neighbors(pos: tuple[int, int]):
            x, y = pos
            return [
                (xx, yy)
                for (xx, yy) in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
                if 0 <= xx < m and 0 <= yy < n and grid[xx][yy] == 1
            ]

        # 初始化一个 grid 同尺寸的 connected
        seen = [[0 for _ in range(n)] for _ in range(m)]
        connectivity = [[0 for _ in range(n)] for _ in range(m)]

        def is_visited(pos: tuple[int, int]) -> bool:
            return seen[pos[0]][pos[1]] == 1

        def dfs(pos: tuple[int, int]):
            # 从起点开始标记连通的 island
            # print(f"dfs {pos=}")
            stack = [pos]  # 待扩展的 island

            while stack:
                stack_item = stack.pop()
                x, y = stack_item
                connectivity[x][y] = 1
                seen[x][y] = 1
                for neighbor in get_island_neighbors(stack_item):
                    if is_visited(neighbor):
                        # print(f"is visited {neighbor=}")
                        continue
                    # print(f"processing {neighbor=}")
                    ni, nj = neighbor
                    seen[ni][nj] = 1
                    stack.append(neighbor)
                    # print(f"adding {connected_islands=} to queue")

        # 针对 islands_on_edge 进行 dfs 标记
        for island_on_edge in islands_on_edge:
            dfs(island_on_edge)

        def print_grid(_grid):
            print("-----------")
            for row in _grid:
                print("\t".join(map(str, row)))
            print("-----------")

        # print_grid(seen)
        # print_grid(connectivity)

        return total_island_count - sum([sum(row) for row in connectivity])


# @lc code=end
