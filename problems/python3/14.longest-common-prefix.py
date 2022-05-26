#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        common_prefix = ""
        for num in zip(*strs):
            if len(set(num)) == 1:
                common_prefix += num[0]
            else:
                return common_prefix
        return common_prefix


# @lc code=end
