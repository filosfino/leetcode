#
# @lc app=leetcode.cn id=381 lang=python3
#
# [381] O(1) 时间插入、删除和获取随机元素 - 允许重复
#
# https://leetcode.cn/problems/insert-delete-getrandom-o1-duplicates-allowed/description/
#
# algorithms
# Hard (42.90%)
# Likes:    248
# Dislikes: 0
# Total Accepted:    24.3K
# Total Submissions: 56.8K
# Testcase Example:  '["RandomizedCollection","insert","insert","insert","getRandom","remove","getRandom"]\n' + '[[],[1],[1],[2],[],[1],[]]'
#
# RandomizedCollection 是一种包含数字集合(可能是重复的)的数据结构。它应该支持插入和删除特定元素，以及删除随机元素。
#
# 实现 RandomizedCollection 类:
#
#
# RandomizedCollection()初始化空的 RandomizedCollection 对象。
# bool insert(int val) 将一个 val 项插入到集合中，即使该项已经存在。如果该项不存在，则返回 true ，否则返回 false
# 。
# bool remove(int val) 如果存在，从集合中移除一个 val 项。如果该项存在，则返回 true ，否则返回 false 。注意，如果
# val 在集合中出现多次，我们只删除其中一个。
# int getRandom() 从当前的多个元素集合中返回一个随机元素。每个元素被返回的概率与集合中包含的相同值的数量 线性相关 。
#
#
# 您必须实现类的函数，使每个函数的 平均 时间复杂度为 O(1) 。
#
# 注意：生成测试用例时，只有在 RandomizedCollection 中 至少有一项 时，才会调用 getRandom 。
#
#
#
# 示例 1:
#
#
# 输入
# ["RandomizedCollection", "insert", "insert", "insert", "getRandom", "remove",
# "getRandom"]
# [[], [1], [1], [2], [], [1], []]
# 输出
# [null, true, false, true, 2, true, 1]
#
# 解释
# RandomizedCollection collection = new RandomizedCollection();// 初始化一个空的集合。
# collection.insert(1);// 向集合中插入 1 。返回 true 表示集合不包含 1 。
# collection.insert(1);// 向集合中插入另一个 1 。返回 false 表示集合包含 1 。集合现在包含 [1,1] 。
# collection.insert(2);// 向集合中插入 2 ，返回 true 。集合现在包含 [1,1,2] 。
# collection.getRandom();// getRandom 应当有 2/3 的概率返回 1 ，1/3 的概率返回 2 。
# collection.remove(1);// 从集合中删除 1 ，返回 true 。集合现在包含 [1,2] 。
# collection.getRandom();// getRandom 应有相同概率返回 1 和 2 。
#
#
#
#
# 提示:
#
#
# -2^31 <= val <= 2^31 - 1
# insert, remove 和 getRandom 最多 总共 被调用 2 * 10^5 次
# 当调用 getRandom 时，数据结构中 至少有一个 元素
#
#
#


# @lc code=start

from collections import defaultdict
from random import choice
from typing import NamedTuple


class DataVal(NamedTuple):
    val: int
    list_indices: set[int]


class RandomizedCollection:
    def __init__(self):
        # RandomizedCollection()初始化空的 RandomizedCollection 对象。
        self._data: dict[int, DataVal] = {}
        self._list = []

    def insert(self, val: int) -> bool:
        # bool insert(int val) 将一个 val 项插入到集合中，即使该项已经存在。如果该项不存在，则返回 true ，否则返回 false 。
        self._list.append(val)
        if val in self._data:
            self._data[val].list_indices.add(len(self._list) - 1)
            return False
        else:
            self._data[val] = DataVal(val, {len(self._list) - 1})
            return True

    def remove(self, val: int) -> bool:
        # bool remove(int val) 如果存在，从集合中移除一个 val 项。如果该项存在，则返回 true ，否则返回 false 。注意，如果 val 在集合中出现多次，我们只删除其中一个。
        if not self._data or val not in self._data:
            return False
        data_val = self._data[val]
        list_index_to_remove = data_val.list_indices.pop()
        if not data_val.list_indices:
            self._data.pop(val)

        list_last_index = len(self._list) - 1
        val_filled_in = self._list.pop()
        if list_index_to_remove != list_last_index:
            self._list[list_index_to_remove] = val_filled_in
            self._data[val_filled_in].list_indices.discard(list_last_index)
            self._data[val_filled_in].list_indices.add(list_index_to_remove)
        return True

    def getRandom(self) -> int:
        # int getRandom() 从当前的多个元素集合中返回一个随机元素。每个元素被返回的概率与集合中包含的相同值的数量 线性相关 。
        return choice(self._list)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end
