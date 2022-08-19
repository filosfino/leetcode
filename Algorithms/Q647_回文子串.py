#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#
# https://leetcode.cn/problems/palindromic-substrings/description/
#
# algorithms
# Medium (66.62%)
# Likes:    951
# Dislikes: 0
# Total Accepted:    214.5K
# Total Submissions: 322K
# Testcase Example:  '"abc"'
#
# 给你一个字符串 s ，请你统计并返回这个字符串中 回文子串 的数目。
#
# 回文字符串 是正着读和倒过来读一样的字符串。
#
# 子字符串 是字符串中的由连续字符组成的一个序列。
#
# 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。
#
#
#
# 示例 1：
#
#
# 输入：s = "abc"
# 输出：3
# 解释：三个回文子串: "a", "b", "c"
#
#
# 示例 2：
#
#
# 输入：s = "aaa"
# 输出：6
# 解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
#
#
#
# 提示：
#
#
# 1 <= s.length <= 1000
# s 由小写英文字母组成
#
#
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        ret = 0
        # 寻找中心
        centers = []  # 记录 (start, end) pair
        # 长度为 1 的中心
        centers.extend((x, x) for x in range(len(s)))
        # 长度为 2 的中心
        centers.extend((x, x + 1) for x in range(len(s) - 1) if s[x] == s[x + 1])
        ret += len(centers)

        # 往两边拓展
        # print(centers)
        for center in centers:
            # print(f"processing {center}")
            l, r = center
            while 0 < l and r < len(s) - 1:
                l -= 1
                r += 1
                if s[l] != s[r]:
                    break
                else:
                    ret += 1
                    # print(f"valid extend {l}~{r}: {s[l:r+1]}")
        return ret


# @lc code=end
