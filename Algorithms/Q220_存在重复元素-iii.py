#
# @lc app=leetcode.cn id=220 lang=python3
#
# [220] 存在重复元素 III
#
# https://leetcode-cn.com/problems/contains-duplicate-iii/description/
#
# algorithms
# Medium (25.94%)
# Likes:    164
# Dislikes: 0
# Total Accepted:    16K
# Total Submissions: 61.7K
# Testcase Example:  '[1,2,3,1]\n3\n0'
#
# 给定一个整数数组，判断数组中是否有两个不同的索引 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值最大为 t，并且 i 和 j
# 之间的差的绝对值最大为 ķ。
#
# 示例 1:
#
# 输入: nums = [1,2,3,1], k = 3, t = 0
# 输出: true
#
# 示例 2:
#
# 输入: nums = [1,0,1,1], k = 1, t = 2
# 输出: true
#
# 示例 3:
#
# 输入: nums = [1,5,9,1,5,9], k = 2, t = 3
# 输出: false
#
#

# @lc code=start
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if len(nums) < 2:
            return False
        if t < 0:
            return False
        buckets = {}
        for i in range(len(nums)):
            # 保证一个 bucket 内必然满足条件
            bucket_key = nums[i] // (t + 1)
            if bucket_key in buckets:
                return True
            # 每个 bucket 中只有一个元素，如果出现多个元素，必然已经 return True
            if (bucket_key - 1) in buckets and nums[i] - buckets[bucket_key - 1] <= t:
                return True
            if (bucket_key + 1) in buckets and buckets[bucket_key + 1] - nums[i] <= t:
                return True
            buckets[bucket_key] = nums[i]
            # 把不在 sliding window 的 bucket 清空
            if i >= k:
                bucket_key_to_del = nums[i - k] // (t + 1)
                if bucket_key_to_del in buckets:
                    del buckets[bucket_key_to_del]
        return False


# @lc code=end
