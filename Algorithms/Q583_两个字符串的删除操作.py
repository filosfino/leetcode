#
# @lc app=leetcode.cn id=583 lang=python3
#
# [583] 两个字符串的删除操作
#
# https://leetcode.cn/problems/delete-operation-for-two-strings/description/
#
# algorithms
# Medium (65.63%)
# Likes:    493
# Dislikes: 0
# Total Accepted:    97.3K
# Total Submissions: 148.1K
# Testcase Example:  '"sea"\n"eat"'
#
# 给定两个单词 word1 和 word2 ，返回使得 word1 和  word2 相同所需的最小步数。
#
# 每步 可以删除任意一个字符串中的一个字符。
#
#
#
# 示例 1：
#
#
# 输入: word1 = "sea", word2 = "eat"
# 输出: 2
# 解释: 第一步将 "sea" 变为 "ea" ，第二步将 "eat "变为 "ea"
#
#
# 示例  2:
#
#
# 输入：word1 = "leetcode", word2 = "etco"
# 输出：4
#
#
#
#
# 提示：
#
#
#
# 1 <= word1.length, word2.length <= 500
# word1 和 word2 只包含小写英文字母
#
#
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def get_longest_substring_length(text1, text2):
            m = len(text1)
            n = len(text2)
            dp = [[0] * (n + 1) for _ in range(m + 1)]
            for i in range(m + 1):
                for j in range(n + 1):
                    if i == 0 or j == 0:
                        dp[i][j] = 0
                    elif text1[i - 1] == text2[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    else:
                        dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
            return dp[m][n]

        longest_substring_length = get_longest_substring_length(word1, word2)
        # print(f"longest_substring_length: {longest_substring_length}")
        return len(word1) - longest_substring_length + len(word2) - longest_substring_length


# @lc code=end
